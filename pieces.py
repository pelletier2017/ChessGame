

class ChessPiece:
    def __init__(self, row, col, player):
        self._row = row
        self._col = col
        self._player = player

        self._char = "?"
        self._possible_moves = set()

    def __str__(self):
        return "({} at {}, {})".format(self.__class__.__name__, self._row, self._col)

    def get_char(self):
        """returns single character representation of given chess piece on board"""
        return self._char

    def is_moving(self, r2, c2):
        """returns boolean for if target row, col are not both exactly the same as current row, col"""
        return r2 != self._row or c2 != self._col

    def is_valid_attack(self, board, r2, c2):
        if board.on_board(r2, c2) and board.get_square(r2, c2).lower() != "k":
            defending_square = board.get_square(r2, c2)
            # able to attack,
            # not islower() is to account for "." being valid attack
            if self._player == "p" and not defending_square.islower():
                return True
            elif self._player == "c" and not defending_square.isupper():
                return True
        return False


class Pawn(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "p"

    def calc_moves(self, board):
        """returns set of tuples in form (row, col) that are possible moves"""
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        # player pawn attack upward, comp pawns attack downward
        if self._player == "p":
            r2 = r1 + 1
        else:
            r2 = r1 - 1

        # find pawn spaces it should be able to attack
        for i in (-1, 1):
            c2 = c1 + i
            if self.is_valid_attack(board, r2, c2):
                moves["defender"].add((r2, c2))

        return moves


class Rook(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "r"

    def calc_moves(self, board):
        """returns set of tuples in form (row, col) that are possible moves"""
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        # increment in both directions
        # collision if piece is found break while
        for i in (-1, 1):
            r2 = r1
            c2 = c1

            # check all rows in same col
            while board.on_board(r2, c2):
                
                if board.has_piece_at(r2, c2) and self.is_moving(r2, c2):
                    assert (r2, c2) not in self._possible_moves
                    moves["defender"].add((r2, c2))
                    break
                r2 += i

            r2 = r1
            c2 = c1

            # check all cols in same row
            while board.on_board(r2, c2):
                if board.has_piece_at(r2, c2) and self.is_moving(r2, c2):
                    if not board.has_king_at(r2, c2):
                        moves["defender"].add((r2, c2))
                    assert (r1, c1) not in self._possible_moves
                    break
                c2 += i

        return moves


class Bishop(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "b"

    def calc_moves(self, board):
        """returns set of tuples in form (row, col) that are possible moves"""
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        # i and j are increments for r2 and c2 going in diagonal directions until falling off board
        for i in (-1, 1):
            for j in (-1, 1):
                r2 = r1
                c2 = c1

                while board.on_board(r2, c2):
                    if board.has_piece_at(r2, c2) and self.is_moving(r2, c2):
                        if not board.has_king_at(r2, c2):
                            moves["defender"].add((r2, c2))
                        assert (r1, c1) not in self._possible_moves
                        break
                    r2 += i
                    c2 += j

        return moves


class Queen(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "q"

    def calc_moves(self, board):
        """returns set of tuples in form (row, col) that are possible moves"""
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        # check columns and rows
        for i in (-1, 1):
            r2 = r1
            c2 = c1

            # check all rows in same col
            while board.on_board(r2, c2):
                if board.has_piece_at(r2, c2) and self.is_moving(r2, c2):
                    assert (r2, c2) not in self._possible_moves
                    if not board.has_king_at(r2, c2):
                        moves["defender"].add((r2, c2))
                    break
                r2 += i

            r2 = r1
            c2 = c1

            # check all cols in same row
            while board.on_board(r2, c2):
                if board.has_piece_at(r2, c2) and self.is_moving(r2, c2):
                    assert (r1, c1) not in self._possible_moves
                    if not board.has_king_at(r2, c2):
                        moves["defender"].add((r2, c2))
                    break
                c2 += i

        # check diagonals
        for i in (-1, 1):
            for j in (-1, 1):
                r2 = r1
                c2 = c1

                while board.on_board(r2, c2):
                    if board.has_piece_at(r2, c2) and self.is_moving(r2, c2):
                        if not board.has_king_at(r2, c2):
                            moves["defender"].add((r2, c2))
                        assert (r1, c1) not in self._possible_moves
                        break
                    r2 += i
                    c2 += j

        return moves


class Knight(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "n"

    def calc_moves(self, board):
        """returns set of tuples in form (row, col) that are possible moves"""
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        for i, j in ((1, 2), (2, 1)):
            for i_sign in (-1, 1):
                for j_sign in (-1, 1):
                    r2 = r1 + (i * i_sign)
                    c2 = c1 + (j * j_sign)
                    assert i != j
                    if board.on_board(r2, c2):
                        if all([board.has_piece_at(r2, c2), self.is_moving(r2, c2), not board.has_king_at(r2, c2)]):
                            moves["defender"].add((r2, c2))
                            assert (r1, c1) not in self._possible_moves

        return moves


class King(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "k"

    def calc_moves(self, board):
        """returns set of tuples in form (row, col) that are possible moves"""
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        for i in range(-1, 2):
            for j in range(-1, 2):
                r2 = r1 + i
                c2 = c1 + j
                if self.is_valid_attack(board, r2, c2):
                    moves["defender"].add((r2, c2))
                    assert (r1, c1) not in self._possible_moves

        return moves
