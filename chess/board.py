from chess import helper
from chess import pieces
from chess.pieces import P1_CHAR, P2_CHAR

DEFAULT_BOARD = "1 rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"

piece_class_dict = {"p": pieces.Pawn,
                    "r": pieces.Rook,
                    "b": pieces.Bishop,
                    "q": pieces.Queen,
                    "n": pieces.Knight,
                    "k": pieces.King}

# unfortunately this doesn't print symbols to console
# it remains unused
"""
piece_unicode_dict = {"p": u'\u2659',
                      "r": u'\u2656',
                      "b": u'\u2657',
                      "q": u'\u2655',
                      "n": u'\u2658',
                      "k": u'\u2654',
                      "P": u'\u265F',
                      "R": u'\u265C',
                      "B": u'\u265D',
                      "Q": u'\u265B',
                      "N": u'\u265E',
                      "K": u'\u265A'}
"""


class ChessBoard:
    def __init__(self, board=DEFAULT_BOARD):
        self._str_code = board
        self._player_turn = board[0]
        self._board = tuple(map(tuple, board[2:].split()))

        assert self.sanity_check()

    def __str__(self):
        # creating top border
        top_border = "+---" * 8 + "+\n"

        rows = []
        # creating inner grid
        for i in range(len(self._board) - 1, -1, -1):
            row = ""
            row += top_border
            row += str(i + 1)
            for square in self._board[i]:
                if square != ".":
                    row += " {} |".format(square)
                else:
                    row += "   |"
            rows.append(row)

        # create bottom border
        letters = "abcdefgh"
        bottom_border = ""
        for letter in letters:
            bottom_border += "+-{}-".format(letter)
        bottom_border += "+"
        rows.append(bottom_border)

        # debug bottom border
        # delete this eventually
        debug_border = ""
        for i in range(8):
            debug_border += "  {} ".format(i)
        debug_border += "\n"
        rows.append(debug_border)

        return "\n".join(rows)

    def __repr__(self):
        return self._str_code

    def sanity_check(self):
        """
        Goes through a series of asserts to verify the Board object is
        working properly
        returns: True if all tests pass, otherwise raises assertion errors
        """
        # checks if board is 8x8
        assert len(self._board) == 8, "board does not have 8 rows"
        for row in self._board:
            assert len(row) == 8, "a row does not have 8 entries"

        # checks player turn is "r" or "b"
        assert self._player_turn in (P1_CHAR, P2_CHAR), "player turn: {} error".format(
                                                            self._player_turn)

        # checks all valid squares are valid characters
        for row in self._board:
            for square in row:
                assert square.upper() in ("R", "N", "B", "Q", "K", "P", "."), \
                    "There is a {} in the grid".format(square)

        # check each player has between 0 and 12 pieces
        player_pieces = self.get_piece_count(P1_CHAR)
        assert 0 < player_pieces <= 16, \
            "player cant have {} pieces".format(player_pieces)
        computer_pieces = self.get_piece_count(P2_CHAR)
        assert 0 < computer_pieces <= 16, \
            "computer cant have {} pieces".format(computer_pieces)

        # count kings
        assert self._str_code.count("k") == 1, \
            "player has {} kings".format(self._str_code.count("k"))
        assert self._str_code.count("K") == 1, \
            "computer has {} kings".format(self._str_code.count("K"))

        return True

    def get_player_turn(self):
        """
        Gets the string representation of the player who's turn it is.
        :return: string of 1 number either "1" or "2" for player 1 or player 2
        """
        assert self._player_turn in ("1", "2")
        return self._player_turn

    def get_square(self, row, col):
        """
        Gets the string representation of a piece at given row and col 
        on the board.
        :param row: int
        :param col: int
        :return: string of one letter
        """
        return self._board[row][col]

    def get_piece_count(self, player):
        """
        Counts the number of pieces for a given player.
        :param player: a string representing the player "1" or "2"
        :return: number of pieces as an int
        """
        assert player in (P1_CHAR, P2_CHAR), "invalid player {}".format(player)
        piece_count = 0
        for char in self._str_code[2:]:
            if player == P1_CHAR and char.islower():
                piece_count += 1
            elif player == P2_CHAR and char.isupper():
                piece_count += 1
        return piece_count

    def do_move(self, move):
        """
        Returns a board that is made by performing a given move on the 
        current board. This makes no changes to the current board.
        :param move: a chess move in the form "a1 b2"
        :return: board object
        """
        frm, to = move.split()
        assert self.sanity_check()
        assert len(frm) == 2 and len(to) == 2, "invalid inputs: {} {}" \
            .format(frm, to)
        assert frm[0] in "abcdefgh", "frm letter: {} not valid".format(frm[0])
        assert to[0] in "abcdefgh", "to letter: {} not valid".format(to[0])
        assert frm[1] in "12345678", "frm number: {} not valid".format(frm[1])
        assert to[1] in "12345678", "to number: {} not valid".format(to[1])

        decoded_frm = helper.decode_inpt(frm)
        decoded_to = helper.decode_inpt(to)
        prev_board = self.__repr__().split()[1:]
        assert len(prev_board) == 8, "len of prev board should now be 8"

        r1, c1 = decoded_frm
        r2, c2 = decoded_to

        attacking_piece = self._board[r1][c1]
        defending_piece = self._board[r2][c2]

        if self._player_turn == P1_CHAR:
            assert attacking_piece.islower(), "Error can't attack with this. " \
             "Current player: {}. attacking_piece: {}".format(self._player_turn, attacking_piece)
            assert not defending_piece.islower(), "Error can't attack with this. " \
             "Current player: {}. defending piece: {}".format(self._player_turn, defending_piece)

        elif self._player_turn == P2_CHAR:
            assert attacking_piece.isupper(), "Error can't attack with this. " \
             "Current player: {}. attacking_piece: {}".format(self._player_turn, attacking_piece)
            assert not defending_piece.isupper(), "Error can't attack with this. " \
             "Current player: {}. defending piece: {}".format(self._player_turn, defending_piece)

        # now make new board while changing pieces
        new_board = []
        for r in range(len(prev_board)):
            # if current row doesn't include pieces that will change
            if r != r1 and r != r2:
                new_board.append(prev_board[r])
            else:
                new_row = ""
                for c in range(len(prev_board[r])):
                    if r == r1 and c == c1:
                        new_row += "."
                    elif r == r2 and c == c2:
                        # upgrades pawns to queens if they reach the last row
                        if attacking_piece == "p" and r2 == 7:
                            new_row += "q"
                        elif attacking_piece == "P" and r2 == 0:
                            new_row += "Q"
                        else:
                            new_row += attacking_piece
                    else:
                        new_row += prev_board[r][c]
                new_board.append(new_row)

        # flip players turn
        assert self._player_turn in (P1_CHAR, P2_CHAR)
        if self._player_turn == P1_CHAR:
            new_player_turn = P2_CHAR
        else:
            new_player_turn = P1_CHAR

        new_str = new_player_turn + " " + " ".join(new_board)
        return ChessBoard(new_str)

    def evaluate(self):
        """
        Evaluates current board state by adding up each player's pieces and 
        each piece has a weight. The value returned is current player's score 
        subtracted by the opposite players score. If current player is ahead 
        the score will be positive.
        :return: int
        """
        score_dict = {"p": 1,
                      "n": 3,
                      "b": 3,
                      "r": 5,
                      "q": 9,
                      "k": 0}
        p1_score = 0
        p2_score = 0
        for row in self._board:
            for square in row:
                if square.islower():
                    p1_score += score_dict[square.lower()]
                elif square.isupper():
                    p2_score += score_dict[square.lower()]

        score = p1_score - p2_score

        if self.has_no_moves():
            if self.is_attacking_king(flip_player=True):  # sure its flipped=True?
                # its a checkmate
                if self._player_turn == P1_CHAR:
                    score = -1000
                else:
                    score = 1000
            else:
                # its a draw
                if score > 0:
                    # player1 is ahead in score and does NOT want to draw
                    score = -1000
                else:
                    # player1 is behind in score and DOES want to draw
                    score = 1000

        if self._player_turn == P1_CHAR:
            return score
        else:
            return score * -1

    def calc_possible_moves(self):
        """
        Returns a list of valid chess moves for current player in form "a1 b2"
        :return: list of strings
        """

        possible_moves = []

        # for each piece on the board
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                piece_char = self._board[r][c]
                if piece_char != ".":

                    # checks if either can attack
                    player_can_attack = self._player_turn == P1_CHAR and piece_char.islower()
                    comp_can_attack = self._player_turn == P2_CHAR and self._board[r][c].isupper()

                    # if piece can attack, make a piece object
                    if player_can_attack or comp_can_attack:
                        piece_class = piece_class_dict[piece_char.lower()]
                        piece = piece_class(r, c, self._player_turn)
                        new_moves = piece.calc_moves(self)

                        # add each pieces's moves into possible_moves
                        # in the form "a1 b2"
                        for defender in new_moves["defender"]:
                            frm = helper.encode_inpt(*new_moves["attacker"])
                            to = helper.encode_inpt(*defender)
                            possible_moves.append("{} {}".format(frm, to))

        # filter out any moves that would put the king in check
        i = 0
        while i < len(possible_moves):
            possible_board = self.do_move(possible_moves[i])
            if possible_board.is_attacking_king():
                possible_moves.pop(i)
            else:
                i += 1

        return possible_moves

    def has_no_moves(self):
        """
        Returns True if the current player has no valid moves. Moves that put 
        their king in check are not considered valid moves.
        :return: Boolean
        """
        # for each piece on the board
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                piece_char = self._board[r][c]
                if piece_char != ".":

                    # checks if either can attack
                    player_can_attack = self._player_turn == P1_CHAR and piece_char.islower()
                    comp_can_attack = self._player_turn == P2_CHAR and \
                                      self._board[r][c].isupper()

                    # if piece can attack, make a piece object
                    if player_can_attack or comp_can_attack:
                        piece_class = piece_class_dict[piece_char.lower()]
                        piece = piece_class(r, c, self._player_turn)
                        new_moves = piece.calc_moves(self)

                        # add each pieces's moves into possible_moves
                        # in the form "a1 b2"

                        for defender in new_moves["defender"]:
                            frm = helper.encode_inpt(*new_moves["attacker"])
                            to = helper.encode_inpt(*defender)
                            move = "{} {}".format(frm, to)
                            possible_board = self.do_move(move)
                            if not possible_board.is_attacking_king():
                                return False
        return True

    def on_board(self, row, col):
        """
        Returns boolean for if row and column are within the board
        :param row: int
        :param col: int
        :return: Boolean
        """
        num_rows = len(self._board)
        num_cols = len(self._board[0])
        within_rows = 0 <= row < num_rows
        within_cols = 0 <= col < num_cols
        return within_rows and within_cols

    def is_square_attacked(self, row, col, static_player=False):
        """
        Returns true is any enemy pieces are threatening this square. 
        Enemy pieces are opposite of current player's turn. If static_player is 
        set to true, the current player on the board will not change depending 
        which piece is checked.
        :param row: int
        :param col: int
        :param static_player: Boolean
        :return: Boolean
        """

        # temporarily flip self._player_turn to the same player
        # as square being attacked
        before_flip = self._player_turn

        if self._board[row][col].islower():
            square_owner = P1_CHAR
        elif self._board[row][col].isupper():
            square_owner = P2_CHAR
        else:
            square_owner = "unknown"

        player_flipped = False
        # if it is unknown, dont change anything
        if square_owner != "unknown" and not static_player:
            if self._player_turn != square_owner:
                player_flipped = True
                if self._player_turn == P1_CHAR:
                    self._player_turn = P2_CHAR
                else:
                    self._player_turn = P1_CHAR

        # go in each direction, check pieces that could be attacking from that direction
        is_attacked = False

        # check 1 square distance for kings
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    attacker_row = row + i
                    attacker_col = col + j
                    if self.on_board(attacker_row, attacker_col)\
                            and self.get_square(attacker_row, attacker_col).lower() == "k"\
                            and self.is_enemy(attacker_row, attacker_col):
                        is_attacked = True
                        break

        # check for pawns
        if self._player_turn == P2_CHAR:
            attacker_row = row - 1
        else:
            attacker_row = row + 1
        for i in (-1, 1):
            attacker_col = col + i
            if self.on_board(attacker_row, attacker_col) \
                    and self.get_square(attacker_row, attacker_col).lower() == "p" \
                    and self.is_enemy(attacker_row, attacker_col):
                is_attacked = True
                break

        # check for knights
        for i in (-2, -1, 1, 2):
            for j in (-2, -1, 1, 2):
                if abs(i) != abs(j):
                    attacker_row = row + i
                    attacker_col = col + j
                    if self.on_board(attacker_row, attacker_col)\
                            and self.get_square(attacker_row, attacker_col).lower() == "n"\
                            and self.is_enemy(attacker_row, attacker_col):
                        is_attacked = True
                        break

        # check horizontal for queens/rooks
        attacker_col = col
        for i in (-1, 1):
            attacker_row = row + i
            while self.on_board(attacker_row, attacker_col):
                if self.get_square(attacker_row, attacker_col).lower() in ("q", "r")\
                        and self.is_enemy(attacker_row, attacker_col):
                    is_attacked = True
                    break
                if self.get_square(attacker_row, attacker_col) != ".":
                    break
                attacker_row += i

        # check vertical for queens/rooks
        attacker_row = row
        for i in (-1, 1):
            attacker_col = col + i
            while self.on_board(attacker_row, attacker_col):
                if self.get_square(attacker_row, attacker_col).lower() in ("q", "r") \
                        and self.is_enemy(attacker_row, attacker_col):
                    is_attacked = True
                    break
                if self.get_square(attacker_row, attacker_col) != ".":
                    break
                attacker_col += i

        # check diagonals for queens/bishops
        for i in (-1, 1):
            for j in (-1, 1):
                attacker_row = row + i
                attacker_col = col + j
                while self.on_board(attacker_row, attacker_col):
                    if self.get_square(attacker_row, attacker_col).lower() in (
                    "q", "b") and self.is_enemy(attacker_row, attacker_col):
                        is_attacked = True
                        break
                    if self.get_square(attacker_row, attacker_col) != ".":
                        break
                    attacker_row += i
                    attacker_col += j

        # if player was flipped, flip it back
        if player_flipped:
            if self._player_turn == P1_CHAR:
                self._player_turn = P2_CHAR
            else:
                self._player_turn = P1_CHAR

        # self._player_turn could have been flipped but will always flip back
        after_flip = self._player_turn
        assert after_flip == before_flip

        return is_attacked

    def is_attacking_king(self, flip_player=False):
        """
        Returns True if the current player is threatening the enemy king.
        :param flip_player: If True, searches for if current player king is 
               being attacked by the enemy/
        :return: Boolean
        """

        # king char is flipped from standard king
        # this is to test if you moved into check
        if flip_player:
            if self._player_turn == P1_CHAR:
                enemy_king = "k"
            else:
                enemy_king = "K"
        else:
            if self._player_turn == P1_CHAR:
                enemy_king = "K"
            else:
                enemy_king = "k"

        # find the king
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                if self._board[r][c] == enemy_king:
                    king_row = r
                    king_col = c

        return self.is_square_attacked(king_row, king_col)

    def is_enemy(self, row, col):
        """
        Returns True if a given piece is one of your opponent's pieces 
        according to who's turn it is currently.
        :param row: int
        :param col: int
        :return: Boolean
        """
        if self._player_turn == P1_CHAR and self._board[row][col].isupper():
            return True
        elif self._player_turn == P2_CHAR and self._board[row][col].islower():
            return True
        return False

