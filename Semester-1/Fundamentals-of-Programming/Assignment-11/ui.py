from domain import *
from game import TheGame
from ai import *
from settings import Settings


class UI:
    def __init__(self):
        self._game = None

    def print_recent_moves_of_the_players(self):
        """
            This function prints the last moves of both players.
        """
        for move in self._game.last_moves_list:
            print(move)
        self._game.clear_moves_history()

    def print_boards(self):
        """
            This function prints the boards of both players.
        """
        print("THE BOARD OF THE PLAYER - Computer guesses here:\n{0}".format(self._game.player_board))
        print("THE BOARD OF THE COMPUTER - You guess here:\n{0}".format(self._game.computer_board))
        self.print_recent_moves_of_the_players()
        print("{0} cells left for the player".format(self._game.computer_board.remaining_ship_cells))
        print("{0} cells left for the computer".format(self._game.player_board.remaining_ship_cells))

    def print_finished_boards(self):
        """
            If one player wins, this function prints the boards of both players without hiding the ships and
        a message announcing the winner.
        """
        print("THE BOARD OF THE PLAYER - Computer guesses here:\n{0}".format(self._game.player_board.show_unhidden_board()))
        print("THE BOARD OF THE COMPUTER - You guess here:\n{0}".format(self._game.computer_board.show_unhidden_board()))
        self.print_recent_moves_of_the_players()
        if self._game.computer_board.are_all_ships_found():
            print("CONGRATULATIONS ! YOU WON THE GAME !")
        if self._game.player_board.are_all_ships_found():
            print("Computer wins. You lost the game.")

    @staticmethod
    def _place_player_ships():
        print("You need to place the ships on your board! ")
        print("Would you like to generate their positions randomly? ")
        print("Enter y for YES or n for NO:")
        while True:
            command = input("Write your choice > ")
            if command.lower() not in ("y", "n"):
                if command.lower() == "exit":
                    print("You cannot exit the game now !")
                print("Invalid choice ! Try again !")

                continue
            if command.lower() == "y":
                ships_list = generate_random_ships()
            else:
                ships_list = []
                for ship in SHIPS_NAMES_DICTIONARY:
                    number_of_ships_from_a_category = 1
                    while number_of_ships_from_a_category > 0:
                        print("Enter the coordinates of the {0}. \n{0} has {1} cells.".format(SHIPS_NAMES_DICTIONARY[ship],
                                                                                              SHIPS_LENGTH_DICTIONARY[ship]))
                        start_pair = None
                        end_pair = None
                        while True:
                            start_position_string = input("Enter the start coordinate of the {0}: ".format(SHIPS_NAMES_DICTIONARY[ship]))
                            try:
                                if start_position_string.lower() == "exit":
                                    raise BoardError("You cannot exit the game now !")
                                start_pair = string_to_pair(start_position_string)
                                break
                            except BoardError as error_message:
                                print(error_message)
                                continue

                        while True:
                            end_position_string = input("Enter the end coordinate of the {0}: ".format(SHIPS_NAMES_DICTIONARY[ship]))
                            try:
                                if end_position_string == "exit":
                                    raise BoardError("You cannot exit the game now !")
                                end_pair = string_to_pair(end_position_string)
                                break
                            except BoardError as error_message:
                                print(error_message)
                                continue

                        try:
                            the_ship = Ship(start_pair, end_pair)
                            if len(the_ship) != SHIPS_LENGTH_DICTIONARY[ship]:
                                raise ShipError("Invalid length of the ship !")
                            ships_list.append(the_ship)
                            break
                        except ShipError as error_message:
                            print(error_message)
                            pass
                    number_of_ships_from_a_category -= 1
            return ships_list

    @staticmethod
    def print_the_text_for_the_beginning_of_the_game():
        print("Welcome to my BATTLESHIPS game !")

    def start(self):
        ai_type = {"easy": SimplestAI, "normal": BetterAI, "advanced": TheBestAI}[Settings().ai_type()]
        who_moves_first = {"player": PLAYER, "computer": COMPUTER,
                           "random": random.choice((PLAYER, COMPUTER))}[Settings().who_moves_first()]
        computer_board = Board()
        self.print_the_text_for_the_beginning_of_the_game()
        player_board = Board(owner=PLAYER, ships_list=self._place_player_ships())
        self._game = TheGame(ai_type, player_board, computer_board, who_moves_first)

        while True:
            if self._game.player_board.are_all_ships_found():
                self.print_finished_boards()
                return
            if self._game.computer_board.are_all_ships_found():
                self.print_finished_boards()
                return
            if self._game.whose_turn_is == PLAYER:
                self.print_boards()
                while True:
                    the_pair_for_the_move = input("Your move is: ")
                    if the_pair_for_the_move.lower() == "exit":
                        print("You have quit the game ! COMPUTER WINS !")
                        return
                    try:
                        self._game.player_moves(string_to_pair(the_pair_for_the_move))
                        break
                    except Exception as error_message:
                        print(error_message)
            else:
                self._game.ai_moves()
