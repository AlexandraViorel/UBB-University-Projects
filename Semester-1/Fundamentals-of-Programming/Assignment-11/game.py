from constants import *


class TheGame:
    def __init__(self, ai_type, player_board, computer_board, who_is_first):
        """
            This is the "repository" of the game.
        :param ai_type: the type of AI
        :param player_board: the board of the player
        :param computer_board: the board of the AI
        :param who_is_first: who moves first
        """
        self._ai_type = ai_type
        self._player_board = player_board
        self._computer_board = computer_board
        self._whose_turn_is = who_is_first
        self.last_moves_list = []
        
    @property
    def ai_type(self):
        return self._ai_type

    @property
    def player_board(self):
        return self._player_board

    @property
    def computer_board(self):
        return self._computer_board

    @property
    def whose_turn_is(self):
        return self._whose_turn_is

    def player_moves(self, pair):
        """
            This function executes the move of the player.
        :param pair: the pair of coordinates for the move
        """
        is_it_hit = self._computer_board.make_a_move(pair)
        if not is_it_hit:
            self._whose_turn_is = COMPUTER
        self.last_moves_list.append("Player {0} on {1}{2}".format("HIT" if is_it_hit else "MISS", chr(ord("A") +
                                                                                                      pair[0]),
                                                                  pair[1] + 1))

    def ai_moves(self):
        """
            This function executes the move of the AI.
        """
        while True:
            ai_chooses_a_pair = self._ai_type(self._player_board).choose_the_next_move()
            is_it_hit = self._player_board.make_a_move(ai_chooses_a_pair)
            self.last_moves_list.append("Computer {0} on {1}{2}".format("HIT" if is_it_hit else "MISS",
                                                                        chr(ord("A") + ai_chooses_a_pair[0]),
                                                                        ai_chooses_a_pair[1] + 1))
            if not is_it_hit or self._player_board.are_all_ships_found():
                break
        self._whose_turn_is = PLAYER

    def clear_moves_history(self):
        self.last_moves_list.clear()
