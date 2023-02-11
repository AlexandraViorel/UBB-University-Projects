import random
from constants import *


class SimplestAI:
    """
        This AI hits totally random.
    """
    def __init__(self, board):
        self._board = board

    def give_a_pair_of_coordinates_for_a_move(self):
        the_pair_of_coordinates = [random.randrange(self._board.width), random.randrange(self._board.height)]
        while self._board[the_pair_of_coordinates] not in (SHIP_CELL, EMPTY_CELL):
            the_pair_of_coordinates = [random.randrange(self._board.width), random.randrange(self._board.height)]
        return the_pair_of_coordinates


class BetterAI:
    """
        This AI is better because:
            - when choosing a random move, it only goes on the cells that have the sum of their coordinates a even
            number
            - when it hits, it targets the next move by going left - right and up - down.
    """
    def __init__(self, board):
        self._board = board

    def choose_the_next_move_randomly(self):
        the_pair_of_coordinates = [random.randrange(self._board.width), random.randrange(self._board.height)]
        while self._board[the_pair_of_coordinates] not in (SHIP_CELL, EMPTY_CELL) or (the_pair_of_coordinates[0] + the_pair_of_coordinates[1]) % 2 == 1:
            the_pair_of_coordinates = [random.randrange(self._board.width), random.randrange(self._board.height)]
        return the_pair_of_coordinates

    @staticmethod
    def left_cell(pair):
        return [pair[0], pair[1] + 1]

    @staticmethod
    def right_cell(pair):
        return [pair[0], pair[1] - 1]

    @staticmethod
    def top_cell(pair):
        return [pair[0] + 1, pair[1]]

    @staticmethod
    def bottom_cell(pair):
        return [pair[0] - 1, pair[1]]

    def is_the_pair_valid(self, pair):
        if pair[0] in range(self._board.height) and pair[1] in range(self._board.width):
            return True
        return False

    def target_a_possible_hit_cell(self, given_cell):
        is_it_placed_horizontal = True
        is_it_placed_vertical = True

        def try_a_direction(direction, pair):
            next_cell = direction(pair)
            while self.is_the_pair_valid(next_cell) and self._board[next_cell] == HIT_CELL:
                next_cell = direction(next_cell)
            if self.is_the_pair_valid(next_cell) and self._board[next_cell] in (SHIP_CELL, EMPTY_CELL):
                return next_cell
            return None

        def go_horizontal():
            trying_the_left_cell = try_a_direction(self.left_cell, given_cell)
            if trying_the_left_cell is not None:
                return trying_the_left_cell

            trying_the_right_cell = try_a_direction(self.right_cell, given_cell)
            if trying_the_right_cell is not None:
                return trying_the_right_cell

            return None

        def go_vertical():
            trying_the_top_cell = try_a_direction(self.top_cell, given_cell)
            if trying_the_top_cell is not None:
                return trying_the_top_cell

            trying_the_bottom_cell = try_a_direction(self.bottom_cell, given_cell)
            if trying_the_bottom_cell is not None:
                return trying_the_bottom_cell

            return None

        left_cell = self.left_cell(given_cell)
        right_cell = self.right_cell(given_cell)
        top_cell = self.top_cell(given_cell)
        bottom_cell = self.bottom_cell(given_cell)

        if (self.is_the_pair_valid(left_cell) and self._board[left_cell] == HIT_CELL) or\
                (self.is_the_pair_valid(right_cell) and self._board[right_cell] == HIT_CELL):
            is_it_placed_vertical = False

        if (self.is_the_pair_valid(top_cell) and self._board[top_cell] == HIT_CELL) or\
                (self.is_the_pair_valid(bottom_cell) and self._board[bottom_cell] == HIT_CELL):
            is_it_placed_horizontal = False

        if is_it_placed_horizontal:
            trying_to_go_horizontal = go_horizontal()
            if trying_to_go_horizontal is not None:
                return trying_to_go_horizontal

        if is_it_placed_vertical:
            trying_to_go_vertical = go_vertical()
            if trying_to_go_vertical is not None:
                return trying_to_go_vertical

    def choose_the_next_move(self):
        for i in range(self._board.width):
            for j in range(self._board.height):
                if self._board[[i, j]] == HIT_CELL:
                    return self.target_a_possible_hit_cell([i, j])
        return self.choose_the_next_move_randomly()


class TheBestAI(BetterAI):
    """
        This is the best AI because:
            - when choosing a random move, it generates a heat map, with all the possible placements of all the ships,
            then the list with the cells that have the maximum heat value and then it chooses one of this cells randomly
    """
    def __init__(self, board):
        BetterAI.__init__(self, board)

    def generate_heat_map(self):
        heat_map = [[0 for _ in range(self._board.width)] for __ in range(self._board.height)]
        for a_ship in self._board.ships_list:
            for direction in (self.top_cell, self.bottom_cell, self.left_cell, self.right_cell):
                for i in range(self._board.height):
                    for j in range(self._board.width):
                        good_pair = True
                        cell = [i, j]
                        visited = []
                        for cell_of_ship in range(len(a_ship)):
                            if not self.is_the_pair_valid(cell) or self._board[cell] not in (SHIP_CELL, EMPTY_CELL):
                                good_pair = False
                                break
                            visited.append([i, j])
                            cell = direction(cell)
                        if good_pair:
                            for iterated_cell in visited:
                                heat_map[iterated_cell[0]][iterated_cell[1]] += 1
        return heat_map

    def generate_list_of_best_positions_to_hunt(self):
        heat_map = self.generate_heat_map()
        maximum_heat_value = 0
        choices_list = []
        for i in range(self._board.height):
            for j in range(self._board.width):
                if self._board[[i, j]] in (EMPTY_CELL, SHIP_CELL):
                    maximum_heat_value = max(maximum_heat_value, heat_map[i][j])
        for i in range(self._board.height):
            for j in range(self._board.width):
                if heat_map[i][j] == maximum_heat_value and self._board[[i, j]] in (EMPTY_CELL, SHIP_CELL):
                    choices_list.append([i, j])
        return choices_list

    def choose_the_next_move_randomly(self):
        choices_list = self.generate_list_of_best_positions_to_hunt()
        the_choice = random.choice(choices_list)
        return the_choice
