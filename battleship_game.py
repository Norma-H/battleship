#!/usr/bin/env python3

''' This is a game of Battleship, meant for 2 players.
    After entering players' names, each player will be asked to enter the locations for their ships on their board.
    When one player is asked to enter the location information for their ships, the other player should not be looking
    or present while that player is entering the information through the terminal.
    When the game starts, the players take turns entering locations to launch a missile and try to hit the opposing
    player's ships.
    The first player to hit all the locations and sink all the opponent's ships, wins the game.
    There are a bunch of "to-do" comments for additional features to be added in the future. This is a working minimum
    viable product. '''


class Ship(object):
    ''' This class is to initialize each of the 5 types of ships.
        One ship should be initialized at a time.
        This class holds the name and length for a given ship.
        The following are valid ship names: Carrier, Battleship, Destroyer, Submarine, Patrol Boat. '''
    def __init__(self, name):
        # TODO: verify that the ship name passed to this Class is one of the 5 valid names
        self.ship_name = name
        self.ship_length = {'Carrier': 5, 'Battleship': 4, 'Destroyer': 3, 'Submarine': 3, 'Patrol Boat': 2}

    def length(self):
        return self.ship_length[self.ship_name]

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
        # TODO: confirm that (1) a location was not used for another ship in the same fleet, and
        # TODO: (2) the locations for a specific ship are consecutive.
        # TODO: move print statement out of the Class and have this function return a value
        if ship.ship_length[ship.ship_name] == len(locations):
            for one_location in locations:
                if one_location not in self.board:
                    print(f'{one_location} is an invalid location. Please re-enter your locations.')
                    break
            else:
                self.ships[ship.ship_name] = [one_location for one_location in locations]
        else:
            print(f'Please enter {ship.ship_length[ship.ship_name]} locations for {ship.ship_name} ship.')

    def __repr__(self):
        ''' The output for this function looks like the following:
            Carrier: [5 printed locations outside of a list]
            Battleship: [4 printed locations outside of a list]
            Destroyer: [3 printed locations outside of a list]
            Submarine: [3 printed locations outside of a list]
            Patrol Boat: [2 printed locations outside of a list] '''
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
    # TODO: move this function into the Board Class
    for key, locations in victim.ships.items():
        if target in locations:
            locations.remove(target)
            victim.ships[key] = locations
            result = "HIT!"
            if not locations:
                del(victim.ships[key])
                result = f"You sunk {victim.name}'s {key}!"
            return result
    else:
        return "MISS."


def set_up_locations(player1, player2, ship1, ship2, ship3, ship4, ship5):
    ''' This function asks each player to enter locations for each of their ships and adds them to their board.'''
    # TODO: move this function into the Board class
    for one_player in [player1, player2]:
        for one_ship in [ship1, ship2, ship3, ship4, ship5]:
            while not one_player.ships[one_ship.ship_name]:
                locations = input(f'{one_player.name}, enter {one_ship.ship_length[one_ship.ship_name]} locations for {one_ship.ship_name} (separated by spaces): ').strip().split(' ')
                one_player.add_ship_locations(one_ship, *locations)
        # print(f'Here are the locations of your ships:\n{one_player}\n') #--prints out all entered locations to screen


def play_game(player1, player2):
    ''' This function is to play the game.
        It takes in both players' board information.
        It asks each player one at a time for a next target (launch) towards their opponent and calls the launches
        function.
        It returns a string indicating the player who has won the game. '''
    while True:
        # TODO: keep track of all guesses to tell the user if they repeated
        target1 = input(f"{player1.name}, what's your next target? ")
        result = launches(player2, target1)
        print(result)
        if player2.ships == {}:
            winner = player1.name
            break
        target2 = input(f"{player2.name}, what's your next target? ")
        result = launches(player1, target2)
        print(result)
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

    game_outcome = play_game(player1, player2)

    print(game_outcome)


if __name__ == '__main__':
    main()