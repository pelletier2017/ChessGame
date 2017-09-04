import unittest
import sys

sys.path.append("../")
from chess.board import ChessBoard
import chess.player as player


class TestBasicMinimax(unittest.TestCase):
    def test_simple_board(self):
        board = ChessBoard(
            "1 ........ ........ ........ ........ ........ .....pk. ......p. ......K.")
        p1 = player.BasicMinimax()
        possible_moves = board.calc_possible_moves()

        actual = p1.choose_move(board, possible_moves, depth=3)
        expected = "f6 f7"

        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
