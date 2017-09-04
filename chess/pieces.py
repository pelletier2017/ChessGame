P1_CHAR = "1"
P2_CHAR = "2"


class ChessPiece(object):
    """
    This class is used entirely for inheretence for other chess piece classes.
    """
    def __init__(self, row, col, player):
        assert 0 <= row < 8
        assert 0 <= col < 8
        assert player in (P1_CHAR, P2_CHAR), "player: {} error".format(player)

        self._row = row
        self._col = col
        self._player = player

        self._char = "?"

    def __str__(self):
        return "({} at {}, {})".format(self.__class__.__name__, self._row, self._col)

    def get_char(self):
        """
        Returns single character representation of given chess piece on board.
        If the piece is owned by player1, it will be lowercase. Otherwise 
        it will be uppercase.
        :return: string of 1 letter
        """
        if self._player == P1_CHAR:
            return self._char
        else:
            return self._char.upper()

    def is_moving(self, r2, c2):
        """
        Returns boolean for if target row, col are not both exactly the 
        same as current row, col of the chess piece.
        :param r2: int
        :param c2: int
        :return: Boolean
        """
        return r2 != self._row or c2 != self._col

    def is_valid_attack(self, board, r2, c2):
        """
        Determines if an attack is valid based on a few criteria:
        target square is on the board,
        target square is not a king (of either side)
        and the defending square is on the opposite team of the current square.
        :param board: board object
        :param r2: int
        :param c2: int
        :return: Boolean
        """
        if board.on_board(r2, c2) and board.get_square(r2, c2).lower() != "k":
            defending_square = board.get_square(r2, c2)

            # able to attack
            # not islower() is used here to account for "." being valid attack
            if self._player == P1_CHAR and not defending_square.islower():
                return True
            elif self._player == P2_CHAR and not defending_square.isupper():
                return True
        return False


class Pawn(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "p"

    def calc_moves(self, board):
        """
        returns a dictionary mapping "attacker" to a tuple indicating 
        row and col of the attacking piece and a set of tuples indicating 
        row and column of valid moves. This will include moves that put the 
        king in check which will be filtered out later.
        """
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        # player pawn attack upward, comp pawns attack downward
        if self._player == P1_CHAR:
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


class Knight(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "n"

    def calc_moves(self, board):
        """
        returns a dictionary mapping "attacker" to a tuple indicating 
        row and col of the attacking piece and a set of tuples indicating 
        row and column of valid moves. This will include moves that put the 
        king in check which will be filtered out later.
        """
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


class Bishop(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "b"

    def calc_moves(self, board):
        """
        returns a dictionary mapping "attacker" to a tuple indicating 
        row and col of the attacking piece and a set of tuples indicating 
        row and column of valid moves. This will include moves that put the 
        king in check which will be filtered out later.
        """
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


class Rook(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "r"

    def calc_moves(self, board):
        """
        returns a dictionary mapping "attacker" to a tuple indicating 
        row and col of the attacking piece and a set of tuples indicating 
        row and column of valid moves. This will include moves that put the 
        king in check which will be filtered out later.
        """
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


class Queen(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "q"

    def calc_moves(self, board):
        """
        returns a dictionary mapping "attacker" to a tuple indicating 
        row and col of the attacking piece and a set of tuples indicating 
        row and column of valid moves. This will include moves that put the 
        king in check which will be filtered out later.
        """
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


class King(ChessPiece):
    def __init__(self, row, col, player):
        ChessPiece.__init__(self, row, col, player)
        self._char = "k"

    def calc_moves(self, board):
        """
        returns a dictionary mapping "attacker" to a tuple indicating 
        row and col of the attacking piece and a set of tuples indicating 
        row and column of valid moves. This will include moves that put the 
        king in check which will be filtered out later.
        """
        r1 = self._row
        c1 = self._col

        moves = {"attacker": (r1, c1), "defender": set()}

        # find possible king moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                r2 = r1 + i
                c2 = c1 + j
                if self.is_valid_attack(board, r2, c2) \
                        and not board.is_square_attacked(r2, c2, static_player=True):
                    moves["defender"].add((r2, c2))
                    assert (r1, c1) not in moves["defender"]
        return moves

