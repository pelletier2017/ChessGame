import unittest
import sys

sys.path.append("../")
from chess.board import ChessBoard
import chess.player as player


class TestPlayer(unittest.TestCase):
    def test_repr(self):
        p1 = player.Player("Jeff")
        self.assertEqual("Player(Jeff)", repr(p1))

    def test_minimax_repr(self):
        p1 = player.BasicMinimax("Jeff")
        self.assertEqual("BasicMinimax(Jeff)", repr(p1))


class TestBasicMinimax(unittest.TestCase):
    def test_1_step_checkmate(self):
        board = ChessBoard(
            "1 ........ ........ ........ ........ ........ .....pk. ......p. ......K.")
        p1 = player.BasicMinimax()
        possible_moves = board.calc_possible_moves()

        actual = p1.choose_move(board, depth=1)
        expected = "f6 f7"

        self.assertEqual(actual, expected)

    def test_2_step_checkmate(self):
        # chooses to checkmate in 2 moves instead of taking a queen
        board = ChessBoard(
            "1 k....... ........ r......Q ........ ........ ........ .....PPP B.....K.")
        p1 = player.BasicMinimax()
        possible_moves = board.calc_possible_moves()

        actual = p1.choose_move(board, depth=3)
        expected = "a3 a8"

        self.assertEqual(actual, expected)


class TestRandomChoice(unittest.TestCase):
    def test_choice_in_moves(self):
        board = ChessBoard(
            "1 k....... ........ r......Q ........ ........ ........ .....PPP B.....K.")
        p1 = player.RandomComputer()
        possible_moves = board.calc_possible_moves()

        random_move = p1.choose_move(board)
        self.assertIn(random_move, possible_moves)

if __name__ == "__main__":
    unittest.main()
