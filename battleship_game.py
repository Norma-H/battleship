#!/usr/bin/env python3

''' This is a game of Battleship, meant for 2 players.
    After entering players' names, each player will be asked to enter the locations for their ships on their board.
    When one player is asked to enter the location information for their ships, the other player should not be looking
    or present while that player is entering the information through the terminal.
    When the game starts, the players take turns entering locations to launch a missile and try to hit the opposing
    player's ships.
    The first player to hit all the locations and sink all the opponent's ships, wins the game.'''


class Ship(object):
    ''' This class is to initialize each of the 5 types of ships.
        One ship should be initialized at a time.
        This class holds the name and length for a given ship.
        The following are valid ship names: Carrier, Battleship, Destroyer, Submarine, Patrol Baot. '''
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
    ''' This class is to initialize a board for each player.
        It creates all the locations possible for the board and a dictionary of lists to hold the locations of each ship
        on the board of each player.
        This class adds the locations of each ship as a list to the key of the respective ship in the dictionary. '''
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


def launches(victim, target):
    ''' This function takes in the player that is being attacked and the target by the opponent.
        If the target is an accurate ship location, then that location is removed from the dictionary key.
        If it is the last location in the list and it is removed, then the ship is sunk. '''
    for key,value in victim.ships.items():
        if target in value:
            value.remove(target)
            victim.ships[key] = value
            print("That was a hit!")
            if value == []:
                del(victim.ships[key])
                print(f"You sunk {victim.name}'s {key}!")
                break


def set_up_locations(player1, player2, ship1, ship2, ship3, ship4, ship5):
    ''' This function asks each player to enter locations for each of their ships and adds them to their board.'''
    for one_player in [player1, player2]:
        for one_ship in [ship1, ship2, ship3, ship4, ship5]:
            locations = input(f'{one_player.name}, enter {one_ship.length()} locations for {one_ship.ship_name}: ').strip().split(' ')
            one_player.add_ship_locations(one_ship, *locations)
            # the following line is if an invalid location is entered.
            # this needs to be continuous until the locations entered are valid and correct number
            if one_player.ships[one_ship.ship_name] == []:
                locations = input(f'{one_player.name}, enter {one_ship.length()} locations for {one_ship.ship_name}: ').strip().split(' ')
                one_player.add_ship_locations(one_ship, *locations)
        # print(f'Here are the locations of your ships:\n{one_player}\n')


def play_game(player1, player2):
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
    return f"\n{winner} won! You sunk all your enemy's ships.\nGame over!"


def main():
    ship1 = Ship('Carrier')
    ship2 = Ship('Battleship')
    ship3 = Ship('Destroyer')
    ship4 = Ship('Submarine')
    ship5 = Ship('Patrol Boat')

    name1 = input("Player 1, what is your name? ").strip()
    name2 = input("Player 2, what is your name? ").strip()
    player1 = Board(name1)
    player2 = Board(name2)

    set_up_locations(player1, player2, ship1, ship2, ship3, ship4, ship5)

    print("Let's play!\n")
    # would want to keep track of all guesses to tell the user if they repeated

    game_outcome = play_game(player1, player2)

    print(game_outcome)


if __name__ == '__main__':
    main()