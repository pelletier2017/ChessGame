
class ChessPiece:
    def __init__(self, row, col, player):
        assert 0 <= row < 8
        assert 0 <= col < 8
        assert player in ("p", "c"), "player must be 'p' or 'c'"

        self._row = row
        self._col = col
        self._player = player

        self._char = "?"
        self._possible_moves = set()

    def __str__(self):
        return "({} at {}, {})".format(self.__class__.__name__, self._row, self._col)

    def get_char(self):
        """returns single character representation of given chess piece on board"""
        if self._player == "p":
            return self._char
        else:
            return self._char.upper()

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
            direction = 1
        else:
            direction = -1

        # find diagonal pawn attacks
        r2 = r1 + (1 * direction)
        for i in (-1, 1):
            c2 = c1 + i
            if self.is_valid_attack(board, r2, c2) and board.get_square(r2, c2) != ".":
                    moves["defender"].add((r2, c2))

        # pawn moving 1 upward
        r2 = r1 + (1 * direction)
        c2 = c1
        if self.is_valid_attack(board, r2, c2):
            moves["defender"].add((r2, c2))

        # pawn moving 2 forward (only in 0-based rows 1 and 6
        if r1 == 6 or r1 == 1:
            r2 = r1 + (2 * direction)
            c2 = c1
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

            # check all rows in same col
            r2 = r1 + i
            c2 = c1
            while True:
                if self.is_valid_attack(board, r2, c2):
                    moves["defender"].add((r2, c2))
                    # checks for path block
                    if board.get_square(r2, c2) != ".":
                        break
                else:
                    break
                r2 += i

            # check all cols in same row
            r2 = r1
            c2 = c1 + i
            while True:
                # breaks in that direction if it can attack a piece
                if self.is_valid_attack(board, r2, c2):
                    moves["defender"].add((r2, c2))
                    # checks for path blocked
                    if board.get_square(r2, c2) != ".":
                        break
                else:
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

        # i and j are increments for r2 and c2 going in diagonal directions
        for i in (-1, 1):
            for j in (-1, 1):
                r2 = r1 + i
                c2 = c1 + j

                while True:
                    # go in this diagonal direction until hitting a piece
                    if self.is_valid_attack(board, r2, c2):
                        moves["defender"].add((r2, c2))
                        if board.get_square(r2, c2) != ".":
                            break
                    else:
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
            r2 = r1 + i
            c2 = c1

            # check all rows in same col
            while True:
                if self.is_valid_attack(board, r2, c2):
                    moves["defender"].add((r2, c2))
                    if board.get_square(r2, c2) != ".":
                        break
                else:
                    break
                r2 += i

            r2 = r1
            c2 = c1 + i

            # check all cols in same row
            while True:
                if self.is_valid_attack(board, r2, c2):
                    moves["defender"].add((r2, c2))
                    if board.get_square(r2, c2) != ".":
                        break
                else:
                    break
                c2 += i

        # check diagonals
        for i in (-1, 1):
            for j in (-1, 1):
                r2 = r1 + i
                c2 = c1 + j

                while True:
                    if self.is_valid_attack(board, r2, c2):
                        moves["defender"].add((r2, c2))
                        if board.get_square(r2, c2) != ".":
                            break
                    else:
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
                    if self.is_valid_attack(board, r2, c2):
                        moves["defender"].add((r2, c2))

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

        # find possible king moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                r2 = r1 + i
                c2 = c1 + j
                if self.is_valid_attack(board, r2, c2) \
                        and not board.is_square_attacked(r2, c2, static_player=True): ######################
                    moves["defender"].add((r2, c2))
                    assert (r1, c1) not in moves["defender"]
        print("king moves:", moves)
        return moves


if __name__ == "__main__":
    import test_pieces