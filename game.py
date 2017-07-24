import random

from board import ChessBoard


DEFAULT_BOARD = "rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"

### work in progress

class ChessGame:
    def __init__(self, player1, player2, board=DEFAULT_BOARD, first_move=None):
        self._player1 = player1
        self._player2 = player2

        if first_move is None:
            self._first_move = random.randint(0, 1)
        else:
            self._first_move = first_move

        self._board = ChessBoard(str(self._first_move) + " " + board)

    def play(self):

        board = self._board
        turn_number = 0
        while True:
            print(board)
            turn_number += 1
            if board.is_player_turn():
                # player 1 turn
                possible_moves = board.calc_possible_moves()
                print("{} moves: {}".format(self._player1, possible_moves))

                is_in_check = board.is_attacking_king(flip_player=True)

                # if no possible moves, game is over
                if len(possible_moves) == 0:
                    if is_in_check:
                        # player got check mated
                        winner = self._player2 # or opposite player
                    else:
                        # this is a draw
                        winner = None
                    break
                else:
                    if is_in_check:
                        player1.in_check_message

                board = board.do_move(player1.choose_move(board, possible_moves))

            else:
                # player 2 turn
                possible_moves = board.calc_possible_moves()
                print("{} moves: {}".format(self._player2, possible_moves))

                is_in_check = board.is_attacking_king(flip_player=True)

                # if no possible moves, game is over
                if len(possible_moves) == 0:
                    if is_in_check:
                        # computer got check mated
                        winner = self._player1 # or opposite player
                    else:
                        # this is a draw
                        winner = None
                    break
                else:
                    if is_in_check:
                        player2.in_check_message

                computer_choice = board.best_move(possible_moves)
                board = board.do_move(computer_choice)

        result = {"winner": winner,
                  "turns": turn_number,
                  "final board": board}

        return result

