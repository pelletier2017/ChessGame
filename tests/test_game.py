import unittest
import sys

sys.path.append("../")
from chess.game import ChessGame
import chess.player as player


class TestGame(unittest.TestCase):
    def test_first_move(self):
        p1 = player.RandomComputer()
        p2 = player.OldMinimax()
        game1 = ChessGame(p1, p2, pause=0, first_move=1)
        expected1 = "1 rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"
        self.assertEqual(expected1, repr(game1._board))

        game2 = ChessGame(p1, p2, pause=0, first_move=2)
        expected2 = "2 rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"
        self.assertEqual(expected2, repr(game2._board))

    def test_get_player(self):
        p1 = player.RandomComputer()
        p2 = player.OldMinimax()
        game = ChessGame(p1, p2)
        self.assertEqual(p1, game.get_player1())
        self.assertEqual(p2, game.get_player2())

    def test_get_other_player(self):
        p1 = player.RandomComputer()
        p2 = player.OldMinimax()
        game = ChessGame(p1, p2)
        self.assertEqual(p2, game.get_other_player(p1))
        self.assertEqual(p1, game.get_other_player(p2))

    def test_draw(self):
        board_str = "k....... .R...... .R...... ........ ........ ........ ........ .......K"
        p1 = player.RandomComputer()
        p2 = player.OldMinimax()
        game = ChessGame(p1, p2, first_move=1, board=board_str, verbosity=0)
        result = game.play()
        self.assertEqual(None, result["winner"])

if __name__ == "__main__":
    unittest.main()