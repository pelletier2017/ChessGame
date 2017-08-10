import unittest

from chess.board import ChessBoard
from chess.pieces import (Pawn, Knight, Bishop, Rook, Queen, King,
                          P1_CHAR, P2_CHAR)


class TestPawn(unittest.TestCase):
    def test_movement(self):
        inpt_str = "1 k....... .p...... P.P..... ...p.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (3, 3)
        p1 = Pawn(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(4, 3)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_diagonal_attack(self):
        inpt_str = "1 k....... .p...... P.P..... ...p.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (1, 1)
        p1 = Pawn(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 0), (2, 2), (2, 1), (3, 1)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_computer_diagonal_attack(self):
        inpt_str = "1 k....... .p...... P.P..... ...p.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 0)
        p1 = Pawn(*piece_loc, P2_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(1, 0), (1, 1)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_computer_movement(self):
        inpt_str = "1 k....... .p...... P.P..... ...p.... ........ ........ ...P.... .......K"
        board = ChessBoard(inpt_str)
        piece_loc = (6, 3)
        p1 = Pawn(*piece_loc, P2_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(5, 3), (4, 3)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_attacking_king(self):
        inpt_str = "1 ........ .k...... P.P..... ...p.... ........ ........ ...P.... .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 2)
        p1 = Pawn(*piece_loc, P2_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(1, 2)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)


class TestKnight(unittest.TestCase):
    def test_movement(self):
        inpt_str = "1 k....... ........ .n...... ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 1)
        p1 = Knight(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(4, 0), (0, 2), (1, 3), (3, 3), (4, 2), (4, 0)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_attacking(self):
        inpt_str = "1 k.B..... ........ .n...... ...n.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 1)
        p1 = Knight(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(4, 0), (0, 2), (1, 3), (4, 2), (4, 0)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)


class TestBishop(unittest.TestCase):
    def test_movement(self):
        inpt_str = "1 k....... ....b... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (1, 4)
        p1 = Bishop(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 5), (3, 6), (4, 7), (0, 3), (0, 5),
                                    (2, 3), (3, 2), (4, 1), (5, 0)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_collision(self):
        inpt_str = "1 k....... ....b... ........ ..n..... .N.....b ........ ........ .......K"
        board = ChessBoard(inpt_str)


        piece_loc = (1, 4)
        p1 = Bishop(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 5), (3, 6), (0, 3), (0, 5),
                                    (2, 3)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)


class TestRook(unittest.TestCase):
    def test_movement(self):
        inpt_str = "1 k....... ........ ......r. ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 6)
        p1 = Rook(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                                    (2, 5), (2, 7), (0, 6), (1, 6), (3, 6),
                                    (4, 6), (5, 6), (6, 6), (7, 6)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_collision(self):
        inpt_str = "1 k....... ........ ...P..r. ........ ........ ......p. ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 6)
        p1 = Rook(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 3), (2, 4), (2, 5), (2, 7), (0, 6),
                                    (1, 6), (3, 6), (4, 6)}}
        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)


class TestQueen(unittest.TestCase):
    def test_movement(self):
        inpt_str = "1 k....... ........ ......q. ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 6)
        p1 = Queen(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                                    (2, 5), (2, 7), (0, 6), (1, 6), (3, 6),
                                    (4, 6), (5, 6), (6, 6), (7, 6), (1, 5),
                                    (0, 4), (1, 7), (3, 7), (3, 5), (4, 4),
                                    (5, 3), (6, 2), (7, 1)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_collision(self):
        inpt_str = "1 k....... ......n. .r....q. .....B.. ........ ........ ......P. .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (2, 6)
        p1 = Queen(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 2), (2, 3), (2, 4),
                                    (2, 5), (2, 7), (3, 6),
                                    (4, 6), (5, 6), (6, 6), (1, 5),
                                    (0, 4), (1, 7), (3, 7), (3, 5)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)


class TestKing(unittest.TestCase):
    def test_attack(self):
        inpt_str = "1 k....... B....... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (0, 0)
        p1 = King(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(1, 0), (1, 1)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_movement(self):
        inpt_str = "1 ........ .k...... ........ ........ ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (1, 1)
        p1 = King(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 0), (2, 1), (2, 2), (1, 0), (1, 2), (0, 0), (0, 1), (0, 2)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_attack_angles(self):
        inpt_str = "1 ........ Bkr..... ........ ...N.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (1, 1)
        p1 = King(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 0), (2, 2), (1, 0), (0, 0), (0, 2)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)

    def test_attack_knights(self):
        inpt_str = "1 ........ .k..N... ........ .N.N.... ........ ........ ........ .......K"
        board = ChessBoard(inpt_str)

        piece_loc = (1, 1)
        p1 = King(*piece_loc, P1_CHAR)
        p1_expected = {'attacker': piece_loc,
                       'defender': {(2, 0), (0, 0), (0, 1)}}

        self.assertEqual(board.get_square(*piece_loc), p1.get_char())
        self.assertEqual(p1.calc_moves(board), p1_expected)
