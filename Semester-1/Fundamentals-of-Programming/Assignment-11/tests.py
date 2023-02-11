import unittest
from domain import *
from exceptions import *


class GameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.ship = Ship([1, 1], [1, 5])
        self.board = Board()

    def test_stringToPair__correctInput__TheListWithThePair(self):
        self.assertEqual(string_to_pair("A1"), [0, 0])

    def test_stringToPair__wrongInput__BoardError(self):
        with self.assertRaises(BoardError):
            string_to_pair("A34")

    def test_generateRandomShips__NoInput__ListWith5Ships(self):
        self.assertEqual(len(generate_random_ships()), 5)
        self.assertIsInstance(generate_random_ships()[0], Ship)

    def test_Ship__ShipOfLength5__CorrectStartPositionPair(self):
        self.assertEqual(self.ship.start_position_pair, [1, 1])

    def test_Ship__ShipOfLength5__CorrectEndPositionPair(self):
        self.assertEqual(self.ship.end_position_pair, [1, 5])

    def test_Ship__ShipOfLength5__5OccupiedCells(self):
        self.assertEqual(len(self.ship.occupied_cells), 5)

    def test_LengthOfShip__ShipOfLength5__LengthEqualTo5(self):
        self.assertEqual(len(self.ship), 5)

    def test_BoardInitialization__ARandomGeneratedBoard__CorrectInitializationForHeight(self):
        self.assertEqual(self.board.height, 10)

    def test_BoardInitialization__ARandomGeneratedBoard__CorrectInitializationForWidth(self):
        self.assertEqual(self.board.width, 10)

    def test_BoardInitialization__ARandomGeneratedBoard__CorrectInitializationForShipsList(self):
        self.assertEqual(len(self.board.ships_list), 5)

    def test_BoardInitialization__ARandomGeneratedBoard__CorrectInitializationForRemainingShipCells(self):
        self.assertEqual(self.board.remaining_ship_cells, 17)

    def test_BoardMakeAMove__CorrectInput__NoError(self):
        self.board.make_a_move([1, 1])

    def test_BoardMakeAMove__ACellAlreadyHit__BoardError(self):
        self.board.make_a_move([1, 1])
        with self.assertRaises(BoardError):
            self.board.make_a_move([1, 1])

    def test_BoardIsShipSunk__NoInputAndNoShipSunk__FalseAndNone(self):
        self.assertEqual(self.board.is_ship_sunk(), (False, None))

    def test_BoardAreAllShipsFound__NoInputAndNoShipsFound__False(self):
        self.assertFalse(self.board.are_all_ships_found())

    def test_BoardAreAllShipsFound__NoInputAndAllShipsFound__True(self):
        for i in range(self.board.width):
            for j in range(self.board.height):
                self.board.make_a_move([i, j])
        self.assertTrue(self.board.are_all_ships_found())

    def tearDown(self) -> None:
        pass
