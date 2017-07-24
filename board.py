import pieces
import random

DEFAULT_BOARD = "p rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"

piece_dict = {"p": pieces.Pawn,
              "r": pieces.Rook,
              "b": pieces.Bishop,
              "q": pieces.Queen,
              "n": pieces.Knight,
              "k": pieces.King}


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
            row += str(i) ############################# change this to i - 1 for proper label
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
        bottom_border += "+\n"
        rows.append(bottom_border)

        # delete this eventually
        debug_border = ""
        for i in range(8):
            debug_border += "  {} ".format(i)
        rows.append(debug_border)
        #print(rows)

        return "\n".join(rows)

    def __repr__(self):
        return self._str_code

    def sanity_check(self):
        """
        Goes through a series of asserts to verify the Board object is
        working properly
        returns: True if all tests pass, otherwise None
        """
        # checks if board is 8x8
        assert len(self._board) == 8, "board does not have 8 rows"
        for row in self._board:
            assert len(row) == 8, "a row does not have 8 entries"

        # checks player turn is "r" or "b"
        assert self._player_turn in ("p", "c"), "player turn: {} error".format(
                                                            self._player_turn)

        # checks all valid squares are valid characters
        for row in self._board:
            for square in row:
                assert square.upper() in ("R", "N", "B", "Q", "K", "P", "."), \
                    "There is a {} in the grid".format(square)

        # check each player has between 0 and 12 pieces
        player_pieces = self.get_piece_count("p")
        assert 0 < player_pieces <= 16, \
            "player cant have {} pieces".format(player_pieces)
        computer_pieces = self.get_piece_count("c")
        assert 0 < computer_pieces <= 16, \
            "computer cant have {} pieces".format(computer_pieces)

        # count kings
        assert self._str_code.count("k") == 1, \
            "player has {} kings".format(self._str_code.count("k"))
        assert self._str_code.count("K") == 1, \
            "computer has {} kings".format(self._str_code.count("K"))

        return True

    def is_player_turn(self):
        assert self._player_turn in ("p", "c")
        return self._player_turn == "p"

    def get_square(self, row, col):
        return self._board[row][col]

    def get_piece_count(self, player):
        assert player in ("p", "c"), "invalid player {}".format(player)
        piece_count = 0
        for char in self._str_code[2:]:
            if player == "p" and char.islower():
                piece_count += 1
            elif player == "c" and char.isupper():
                piece_count += 1
        return piece_count

    def do_move(self, move):
        frm, to = move.split()
        assert self.sanity_check()
        assert len(frm) == 2 and len(to) == 2, "invalid inputs: {} {}" \
            .format(frm, to)
        assert frm[0] in "abcdefgh", "frm letter: {} not valid".format(frm[0])
        assert to[0] in "abcdefgh", "to letter: {} not valid".format(to[0])
        assert frm[1] in "12345678", "frm number: {} not valid".format(frm[1])
        assert to[1] in "12345678", "to number: {} not valid".format(to[1])

        decoded_frm = self._decode_inpt(frm)
        decoded_to = self._decode_inpt(to)
        prev_board = self.__repr__().split()[1:]

        r1, c1 = decoded_frm
        r2, c2 = decoded_to

        attacking_piece = self._board[r1][c1]

        assert len(prev_board) == 8, "len of prev board should now be 8"

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
                        new_row += attacking_piece
                    else:
                        new_row += prev_board[r][c]
                new_board.append(new_row)

        # flip players turn
        assert self._player_turn in ("p", "c")
        if self._player_turn == "p":
            new_player_turn = "c"
        else:
            new_player_turn = "p"

        new_str = new_player_turn + " " + " ".join(new_board)
        return ChessBoard(new_str)

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
                    player_can_attack = self._player_turn == "p" and piece_char.islower()
                    comp_can_attack = self._player_turn == "c" and self._board[r][c].isupper()

                    # if piece can attack, make a piece object
                    if player_can_attack or comp_can_attack:
                        piece_class = piece_dict[piece_char.lower()]
                        piece = piece_class(r, c, self._player_turn)
                        new_moves = piece.calc_moves(self)

                        # add each pieces's moves into possible_moves
                        # in the form "a1 b2"
                        for defender in new_moves["defender"]:
                            frm = self._encode_inpt(*new_moves["attacker"])
                            to = self._encode_inpt(*defender)
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

    def best_move(self, possible_moves):
        """
        Later will do more complicated things
        """
        rand_move = random.randrange(len(possible_moves))
        return possible_moves[rand_move]

    def on_board(self, row, col):
        """returns boolean for if the row, col are within the board"""
        num_rows = len(self._board)
        num_cols = len(self._board[0])
        within_rows = 0 <= row < num_rows
        within_cols = 0 <= col < num_cols
        return within_rows and within_cols

    def is_square_attacked(self, row, col, static_player=False):
        """
        Returns true is any enemy pieces are threatening this square. 
        Enemy pieces are opposite of current player's turn.
        :param row: int
        :param col: int
        :return: Boolean
        """

        # temporarily flip self._player_turn to the same player
        # as square being attacked
        before_flip = self._player_turn

        if self._board[row][col].islower():
            square_owner = "p"
        elif self._board[row][col].isupper():
            square_owner = "c"
        else:
            square_owner = "unknown"

        player_flipped = False
        # if it is unknown, dont change anything
        if square_owner != "unknown" and not static_player:
            if self._player_turn != square_owner:
                player_flipped = True
                if self._player_turn == "p":
                    self._player_turn = "c"
                else:
                    self._player_turn = "p"

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
        if self._player_turn == "c":
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

        # check the horizontal
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

        # check the vertical
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

        # check diagonals
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
            if self._player_turn == "p":
                self._player_turn = "c"
            else:
                self._player_turn = "p"

        after_flip = self._player_turn
        # self._player_turn could have been flipped but will always flip back
        assert before_flip == after_flip

        return is_attacked

    def is_attacking_king(self, flip_player=False):
        """
        Returns True if the current player is threatening the enemy king.
        :return: 
        """

        # king char is flipped from standard king
        # this is to test if you moved into check
        if flip_player:
            if self._player_turn == "p":
                enemy_king = "k"
            else:
                enemy_king = "K"
        else:
            if self._player_turn == "p":
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
        if self._player_turn == "p" and self._board[row][col].isupper():
            return True
        elif self._player_turn == "c" and self._board[row][col].islower():
            return True
        return False

    def _decode_inpt(self, inpt_str):
        """
        Converts given input string to row, col
        params: inpt_str is a chess input, ex: "a1"
        returns: tuple with integers row, col
        precondition: letters are lower case between a-h, numbers are 1-8
        """
        letter, num = list(inpt_str)
        row = int(num) - 1
        col = ord(letter) - ord("a")
        return row, col

    def _encode_inpt(self, row, col):
        """
        Converts row, col to chess input, ex "a1"
        params: row, col are integers
        returns 2 char string for chess move with letter, number
        """
        num = str(row + 1)
        letter = chr(col + ord("a"))
        return letter + num


if __name__ == "__main__":
    import test_all