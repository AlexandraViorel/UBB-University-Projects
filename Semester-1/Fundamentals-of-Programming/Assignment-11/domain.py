import random
from exceptions import *
from constants import *
from texttable import Texttable


def string_to_pair(string_pair):
    """
        This functions transforms a given string of a pair into the pair of coordinates that string represents
    for example: if the given string is 'A4' we obtain [0, 3]
    :param string_pair: the given string of a pair
    :return: the pair of coordinates
    """
    pair_of_coordinates = []
    if len(string_pair) > 3 or (len(string_pair) == 3 and string_pair[2] != "0") or len(string_pair) < 2:
        raise BoardError("Invalid coordinates !")
    letter = string_pair[0]
    if not string_pair[1].isnumeric():
        raise BoardError("Invalid coordinates !")
    if len(string_pair) == 2:
        number = int(string_pair[1])
    else:
        number = int(string_pair[1] + string_pair[2])
    if ord(letter) in range(65, 75):  # ASCII codes of A -> J
        pair_of_coordinates.append(ord(letter) - 65)
    elif ord(letter) in range(97, 107):
        pair_of_coordinates.append(ord(letter) - 97)  # ASCII codes of a -> j
    else:
        raise BoardError("Invalid coordinate !")
    if number < 1 or number > 10:
        raise BoardError("Invalid coordinate !")
    else:
        pair_of_coordinates.append(number - 1)
    return pair_of_coordinates


def generate_one_ship_random(occupied_cells_list, height, width, length_of_the_ship):
    """
        This function generates random start and end positions for a ship of given length and returns the ship with
    these coordinates.
    :param occupied_cells_list: the list of occupied cells, in order to generate a good position for the ship
    :param height: the height = 10
    :param width: the width = 10
    :param length_of_the_ship: the given length of the ship
    :return: the ship with the randomly generated positions
    """
    while True:
        orientation = random.choice((10, 11))
        if orientation == VERTICAL:
            start_position_x_coordinate = random.randrange(height)
            start_position_y_coordinate = random.randrange(width - length_of_the_ship + 1)
            end_position_x_coordinate = start_position_x_coordinate
            end_position_y_coordinate = start_position_y_coordinate + length_of_the_ship - 1
        else:
            start_position_x_coordinate = random.randrange(height - length_of_the_ship + 1)
            start_position_y_coordinate = random.randrange(width)
            end_position_x_coordinate = start_position_x_coordinate + length_of_the_ship - 1
            end_position_y_coordinate = start_position_y_coordinate
        is_the_position_of_the_ship_good = True
        for x in range(start_position_x_coordinate, end_position_x_coordinate + 1):
            for y in range(start_position_y_coordinate, end_position_y_coordinate + 1):
                if [x, y] in occupied_cells_list:
                    is_the_position_of_the_ship_good = False
                    break
        if not is_the_position_of_the_ship_good:
            continue
        return Ship([start_position_x_coordinate, start_position_y_coordinate], [end_position_x_coordinate,
                                                                                 end_position_y_coordinate])


def generate_random_ships():
    """
        This function generates 5 random ships positions.
    :return: it returns the list with the 5 ships
    """
    ships_list = []
    occupied_cells_list = []
    height = 10
    width = 10
    for ship in SHIPS_NAMES_DICTIONARY:
        length_of_the_ship = SHIPS_LENGTH_DICTIONARY[ship]
        random_generated_ship = generate_one_ship_random(occupied_cells_list, height, width, length_of_the_ship)
        for occupied_cell in random_generated_ship:
            occupied_cells_list.append(occupied_cell)
        ships_list.append(random_generated_ship)
    return ships_list


class Ship:
    def __init__(self, start_position_pair, end_position_pair):
        if start_position_pair[0] != end_position_pair[0] and start_position_pair[1] != end_position_pair[1]:
            raise ShipError("Invalid bounds for the ship !")
        if start_position_pair[0] > end_position_pair[0]:
            start_position_pair[0], end_position_pair[0] = end_position_pair[0], start_position_pair[0]
        if start_position_pair[1] > end_position_pair[1]:
            start_position_pair[1], end_position_pair[1] = end_position_pair[1], start_position_pair[1]
        self.start_position_pair = start_position_pair
        self.end_position_pair = end_position_pair
        self.occupied_cells = []
        self._create_list_of_occupied_cells()

    def _create_list_of_occupied_cells(self):
        for first_coordinate in range(self.start_position_pair[0], self.end_position_pair[0] + 1):
            for second_coordinate in range(self.start_position_pair[1], self.end_position_pair[1] + 1):
                self.occupied_cells.append([first_coordinate, second_coordinate])

    def __len__(self):
        return len(self.occupied_cells)

    def __iter__(self):
        self._position = -1
        return self

    def __next__(self):
        self._position += 1
        if self._position >= len(self.occupied_cells):
            raise StopIteration
        return self.occupied_cells[self._position]

    def __eq__(self, other):
        if not isinstance(other, Ship):
            return False
        return self.start_position_pair == other.start_position_pair and self.end_position_pair == other.end_position_pair


class Board:
    def __init__(self, owner=COMPUTER, ships_list=None, height=10, width=10):
        self.height = height
        self.width = width
        self.owner_of_the_board = owner
        self.board_matrix = [[EMPTY_CELL for _ in range(self.width)] for __ in range(self.height)]
        if ships_list is None:
            ships_list = generate_random_ships()
        for a_ship in ships_list:
            for ship_cell in a_ship:
                if self[ship_cell] != EMPTY_CELL:
                    raise BoardError("Invalid positions for the ships !")
                self[ship_cell] = SHIP_CELL
        self.ships_list = ships_list
        self.remaining_ship_cells = 17

    def __getitem__(self, item):
        if type(item) is int:
            return self.board_matrix[item]
        return self.board_matrix[item[0]][item[1]]

    def __setitem__(self, item, value):
        if type(item) is int:
            self.board_matrix[item] = value
        self.board_matrix[item[0]][item[1]] = value

    def __str__(self):
        if self.owner_of_the_board == PLAYER:
            return self._board_string(PLAYER_BOARD_SIGNS_DICTIONARY)
        return self._board_string(COMPUTER_BOARD_SIGNS_DICTIONARY)

    def _board_string(self, dictionary_of_signs):
        text_table = Texttable()
        row_list = ["/"]
        for i in range(1, self.width + 1):
            row_list.append(i)
        text_table.add_row(row_list)
        for i in range(self.height):
            row_list = [chr(ord("A") + i)]
            for j in self.board_matrix[i]:
                if self.owner_of_the_board == PLAYER:
                    row_list.append(dictionary_of_signs[j])
                else:
                    row_list.append(dictionary_of_signs[j])
            text_table.add_row(row_list)
        return text_table.draw()

    def show_unhidden_board(self):
        """
        :return: the board with unhidden ships
        """
        return self._board_string(UNHIDDEN_BOARD_SIGNS_DICTIONARY)

    def are_all_ships_found(self):
        """
        :return: it returns TRUE if one of the players found all the ships, so the game ends, else FALSE
        """
        return self.remaining_ship_cells == 0

    def is_ship_sunk(self):
        """
            This function verifies if one of the ships has all of his cells HIT, so that means it is sunk.
        :return: TRUE and the sunk ship, if one of the ships is sunk, else FALSE and NONE
        """
        for ship in self.ships_list:
            it_is_sunk = True
            for occupied_cell in ship:
                if self[occupied_cell] != HIT_CELL:
                    it_is_sunk = False
            if it_is_sunk:
                return True, ship
        return False, None

    def make_a_move(self, pair_of_coordinates):
        """
            This function executes a move. It raises an error if the cell was already HIT, else it verifies if in the
        given cell we have a ship or not and it changes the element from the respective cell.
        :param pair_of_coordinates: the pair of given coordinates for the cell
        :return: it returns TRUE if it hits a ship, else FALSE
        """
        if self[pair_of_coordinates] not in (SHIP_CELL, EMPTY_CELL):
            raise BoardError("This cell is already hit ! Try another one !")
        if self[pair_of_coordinates] == SHIP_CELL:
            self.remaining_ship_cells -= 1
            self[pair_of_coordinates] = HIT_CELL
            is_it_a_sunk_ship, the_sunk_ship = self.is_ship_sunk()
            if is_it_a_sunk_ship:
                for occupied_cell in the_sunk_ship:
                    self[occupied_cell] = SUNK_CELL
                self.ships_list.remove(the_sunk_ship)
            return True
        else:
            self[pair_of_coordinates] = MISS_CELL
            return False
