import random

from board import ChessBoard


DEFAULT_BOARD = "rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"


class ChessGame:
    def __init__(self, player1, player2, board=DEFAULT_BOARD, first_move=None):
        self._player1 = player1
        self._player2 = player2

        if first_move is None:
            self._first_move = random.randint(1, 2)
        else:
            self._first_move = first_move

        self._board = ChessBoard(str(self._first_move) + " " + board)

    def get_player1(self):
        return self._player1

    def get_player2(self):
        return self._player2

    def get_other_player(self, player):
        assert player in (self._player1, self._player2)
        if player == self._player1:
            return self._player2
        else:
            return self._player1

    def play(self):
        board = self._board
        turn_number = 0
        while True:
            turn_number += 1
            print(board)

            # determine whos turn it is
            assert board.get_player_turn() in ("1", "2")
            if board.get_player_turn() == "1":
                player = self._player1
            else:
                player = self._player2

            # determine possible moves
            possible_moves = board.calc_possible_moves()
            print("{} moves: {}".format(player, possible_moves))

            is_in_check = board.is_attacking_king(flip_player=True)

            # if no possible moves, game is over
            if len(possible_moves) == 0:
                if is_in_check:
                    print("{} got check mated".format(player))
                    other_player = self.get_other_player(player)
                    other_player.increment_score()
                    winner = other_player
                else:
                    # this is a draw
                    print("There was a draw!")
                    winner = None
                break
            else:
                if is_in_check:
                    print("{} is in check".format(player))

            board = board.do_move(player.choose_move(board, possible_moves))

        result = {"winner": winner,
                  "turns": turn_number,
                  "final board": board}

        return result

