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


class TestDoMove(unittest.TestCase):
    def test_king_takes(self):
        inpt_str = "1 k....... .P...... ...K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        new_board = board.do_move("a1 b2")
        self.assertEqual(new_board.get_square(1, 1), "k")
        self.assertEqual(new_board.get_square(0, 0), ".")

    def test_multiple_moves(self):
        inpt_str = "1 q.p....k .P...... .R.K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        self.assertEqual(board.get_square(1, 1), "P")
        self.assertEqual(board.get_square(0, 0), "q")
        self.assertEqual(board.get_square(0, 2), "p")
        self.assertEqual(board.get_square(2, 1), "R")

        board2 = board.do_move("a1 b2")
        board3 = board2.do_move("b3 b2")
        board4 = board3.do_move("c1 b2")

        self.assertEqual(board4.get_square(1, 1), "p")
        self.assertEqual(board4.get_square(0, 0), ".")
        self.assertEqual(board4.get_square(0, 2), ".")
        self.assertEqual(board4.get_square(2, 1), ".")

    def test_upgrading_pawn(self):
        inpt_str = "1 q.p....k .P...P.. .R.K.... .......Q ........ ........ .......p ........"
        board = ChessBoard(inpt_str)
        self.assertEqual(board.get_square(6, 7), "p")
        self.assertEqual(board.get_square(7, 7), ".")
        self.assertEqual(board.get_square(1, 5), "P")

        board2 = board.do_move("h7 h8")
        self.assertEqual(board2.get_square(6, 7), ".")
        self.assertEqual(board2.get_square(7, 7), "q")

        board3 = board2.do_move("f2 f1")
        self.assertEqual(board3.get_square(1, 5), ".")
        self.assertEqual(board3.get_square(0, 5), "Q")

    def test_moving_off_board(self):
        inpt_str = "2 q.p....k .P...... .R.K.... .......Q ........ ........ ........ r......."
        board = ChessBoard(inpt_str)
        try:
            board2 = board.do_move("a8 a9")
            self.assert_(False)
        except AssertionError:
            pass

    def test_invalid_inputs(self):
        pass

    def test_piece_invalid_move(self):
        # do_move doesn't care about how far pieces move
        inpt_str = "2 q.p....k .P...... .R.K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        self.assertEqual(board.get_square(2, 1), "R")
        self.assertEqual(board.get_square(1, 1), "P")

    def test_moving_out_of_turn(self):
        inpt_str = "2 q.p....k .P...... .R.K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        try:
            board2 = board.do_move("a1 b2")
            self.assert_(False)
        except AssertionError:
            pass

    def test_attacking_with_empty_square(self):
        inpt_str = "1 ..p....k .P...... .R.K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        try:
            board2 = board.do_move("a1 a2")
            self.assert_(False)
        except AssertionError:
            pass

        try:
            board2 = board.do_move("a1 b2")
            self.assert_(False)
        except AssertionError:
            pass

    def test_taking_own_piece(self):
        inpt_str = "2 q.p....k .P...... .R.K.... .......Q ........ ........ ........ ........"
        board = ChessBoard(inpt_str)
        try:
            board2 = board.do_move("b3 b2")
            self.assert_(False)
        except AssertionError:
            pass




if __name__ == "__main__":
    unittest.main()