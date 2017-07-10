import pieces

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
        bottom_border += "+\n"
        rows.append(bottom_border)

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
        assert self._str_code.count("k") == 1, "player doesn't have a king"
        assert self._str_code.count("K") == 1, "computer doesn't have a king"

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
        possible_moves = []
        for r in range(len(self._board)):
            for c in range(len(self._board[r])):
                if self._board[r][c] != ".":
                    player_can_attack = self._player_turn == "p" and self._board[r][c].islower()
                    comp_can_attack = self._player_turn == "c" and self._board[r][c].isupper()
                    if (player_can_attack and self._player_turn == "p") or \
                            (comp_can_attack and self._player_turn == "c"):
                        piece = piece_dict[self._board[r][c].lower()](r, c, self._player_turn)
                        new_moves = piece.calc_moves(self)
                        for defender in new_moves["defender"]:
                            frm = self._encode_inpt(*new_moves["attacker"])
                            to = self._encode_inpt(*defender)
                            possible_moves.append("{} {}".format(frm, to))

        print(possible_moves)
        return possible_moves

    def best_move(self, possible_moves):
        """
        Later will do more complicated things
        """
        return possible_moves[0]


    def on_board(self, row, col):
        """returns boolean for if the row, col are within the board"""
        num_rows = len(self._board)
        num_cols = len(self._board[0])
        within_rows = 0 <= row < num_rows
        within_cols = 0 <= col < num_cols
        return within_rows and within_cols

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


def main():
    board = ChessBoard("p k....... .......p ........ ........ ........ ........ PPPPPPPP RNBKQBNR")
    print(board)
    print(board.calc_possible_moves())

    #new_board = board.do_move("h2 g3")
    #print()
    #print(new_board)

if __name__ == "__main__":
    main()