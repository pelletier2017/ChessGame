import unittest

from chess.board import ChessBoard


class TestIsSquareAttacked(unittest.TestCase):
    def test_rook_basic_vertical(self):
        inpt_str = "1 k....... ..R..... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_rook_basic_horizontal(self):
        inpt_str = "1 k....... ........ R....... ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_queen_basic_horizontal(self):
        inpt_str = "1 k....... ........ Q....... ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_king_horizontal(self):
        inpt_str = "1 k....... ........ ...K.... ........ ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_bishop_horizontal(self):
        inpt_str = "1 k....... ........ b....... ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertFalse(board.is_square_attacked(2, 2))

    def test_bishop_diagonal(self):
        inpt_str = "1 k....... .B...... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_bishop_diagonal(self):
        inpt_str = "1 k....... .Q...... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_pawn_bad_diagonal(self):
        inpt_str = "1 k....... .P...... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertFalse(board.is_square_attacked(2, 2))

    def test_pawn_good_diagonal(self):
        inpt_str = "1 k....... ........ ........ ...P.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_knight_attack(self):
        inpt_str = "1 k....... ........ ........ ........ ...N.... ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

    def test_knights(self):
        inpt_str = "1 ........ .k..N... ........ .N.N.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 1))
        self.assertTrue(board.is_square_attacked(2, 2))
        self.assertTrue(board.is_square_attacked(1, 0))
        self.assertTrue(board.is_square_attacked(1, 2))
        self.assertTrue(board.is_square_attacked(0, 2))
        self.assertFalse(board.is_square_attacked(2, 0))

    def test_many_safe_neighbors(self):
        inpt_str = "1 k....... .rbr.... .b.b.... .rnr.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertFalse(board.is_square_attacked(2, 2))

    def test_computer_many_safe_neighbors(self):
        inpt_str = "2 k....... .RBR.... .B.B.... .RNR.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertFalse(board.is_square_attacked(2, 2))

    def test_knight_attack(self):
        inpt_str = "2 k....... ........ ........ ........ ...n.... ........ ........ .......K"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_square_attacked(2, 2))

        # add tests for computer's turn


class TestCalcPossibleMoves(unittest.TestCase):
    def test_filtering_moves_that_threaten_king(self):
        inpt_str = "1 k....... b.P..... RP.K.... ........ ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        expected = ["a1 b2"]
        self.assertEqual(board.calc_possible_moves(), expected)

    def test_draw_no_moves(self):
        inpt_str = "1 k....... .R...... ..B..... ........ ........ ........ ........ ...K...."
        board = ChessBoard(inpt_str)
        expected = []
        self.assertEqual(board.calc_possible_moves(), expected)

    def test_player1_got_checkmated(self):
        inpt_str = "1 k....... .Q...... ..B..... ........ ........ ........ ........ ...K...."
        board = ChessBoard(inpt_str)
        expected = []
        self.assertEqual(board.calc_possible_moves(), expected)

    def test_player_in_check_king_takes(self):
        inpt_str = "1 k....... .Q...... ........ ........ r....... ........ ........ ...K...."
        board = ChessBoard(inpt_str)
        expected = ["a1 b2"]
        self.assertEqual(board.calc_possible_moves(), expected)

    def test_computer_in_check_king_takes(self):
        inpt_str = "2 K....... .q...... ........ ........ .....R.. ........ ........ ...k...."
        board = ChessBoard(inpt_str)
        expected = ["a1 b2"]
        self.assertEqual(board.calc_possible_moves(), expected)

    def test_computer_got_checkmated(self):
        inpt_str = "2 K....... .q...... ..b..... ........ ........ ........ ........ ...k...."
        board = ChessBoard(inpt_str)
        expected = []
        self.assertEqual(board.calc_possible_moves(), expected)


class TestIsEnemy(unittest.TestCase):
    def test_player_turn(self):
        inpt_str = "1 k....... .p...... ...K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        self.assertTrue(board.is_enemy(2, 3))
        self.assertTrue(board.is_enemy(3, 7))
        self.assertFalse(board.is_enemy(0, 0))
        self.assertFalse(board.is_enemy(1, 1))

    def test_computer_turn(self):
        inpt_str = "2 k....... .p...... ...K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        self.assertFalse(board.is_enemy(2, 3))
        self.assertFalse(board.is_enemy(3, 7))
        self.assertTrue(board.is_enemy(0, 0))
        self.assertTrue(board.is_enemy(1, 1))


if __name__ == "__main__":
    unittest.main()