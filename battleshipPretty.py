#!/usr/bin/env python3

import pandas as pd
from pandas import Series, DataFrame

class Ship(object):
    def __init__(self, name):
        self.ship_name = name

    def length(self):
        lengths = {'Carrier': 5, 'Battleship': 4, 'Destroyer': 3, 'Submarine': 3, 'Patrol Boat': 2}
        if self.ship_name in lengths.keys():
            self.ship_length = lengths[self.ship_name]
        return self.ship_length

    def __repr__(self):
        return str(self.ship_name)

class Board(object):
    def __init__(self, player_name):
        self.name = player_name
        self.board = set(str(i) + x for i in range(1, 11) for x in 'abcdefghij')
        self.ships = {'Carrier': [], 'Battleship': [], 'Destroyer': [], 'Submarine': [], 'Patrol Boat': []}

    def add_ship_locations(self, ship, *locations):
        # need to also confirm that (1) a location was not used for another ship in the same fleet and
        # (2) the locations for a specific ship are consecutive
        if ship.ship_length == len(locations):
            for one_location in locations:
                if one_location not in self.board:
                    print(f'{one_location} is an invalid location. Please re-enter your locations.')
                    break
            else:
                self.ships[ship.ship_name] = [one_location for one_location in locations]
        else:
            print(f'Please enter {ship.ship_length} locations for {ship.ship_name} ship.')
        return self.ships

    def __repr__(self):
        output = ''
        for ship_key, ship_values in self.ships.items():
            output += f'{ship_key}: '
            for one_value in ship_values:
                output += f'{one_value} '
            output += '\n'
        return output

def create_board():
    df = DataFrame(index=list('abcdefghij'),columns=list(range(1,11)))
    return df

board1 = create_board()
ship1 = Ship('Carrier')
ship2 = Ship('Battleship')
ship3 = Ship('Destroyer')
ship4 = Ship('Submarine')
ship5 = Ship('Patrol Boat')

name1 = input("Player 1, what is your name? ").strip()
name2 = input("Player 2, what is your name? ").strip()
player1 = Board(name1)
player2 = Board(name2)

for one_player in [player1, player2]:
    for one_ship in [ship1, ship2, ship3, ship4, ship5]:
        locations = input(f'{one_player.name}, enter {one_ship.length()} locations for {one_ship.ship_name}: ').strip().split(' ')
        one_player.add_ship_locations(one_ship, *locations)
        # the following line is if an invalid location is entered.
        # this needs to be continuous until the locations entered are valid and correct number
        if one_player.ships[one_ship.ship_name] == []:
            locations = input(f'{one_player.name}, enter {one_ship.length()} locations for {one_ship.ship_name}: ').strip().split(' ')
            one_player.add_ship_locations(one_ship, *locations)
    print(f'Here are the locations of your ships:\n{one_player}\n')

print("Let's play!\n")
hits_by_1 = set()  # instead, would want to keep track of all guesses to tell the user if they repeated
hits_by_2 = set()

def launches(victim, target):
    for key,value in victim.ships.items():
        if target in value:
            value.remove(target)
            victim.ships[key] = value
            print("That was a hit!")
            if value == []:
                del(victim.ships[key])
                print(f"You sunk {victim.name}'s {key}!")
                break

while True:
    target1 = input(f"{player1.name}, what's your next target? ")
    launches(player2, target1)
    if player2.ships == {}:
        winner = player1.name
        break
    target2 = input(f"{player2.name}, what's your next target? ")
    launches(player1, target2)
    if player1.ships == {}:
        winner = player2.name
        break

print(f"\n{winner} won! You sunk all your enemy's ships.\nGame over!")