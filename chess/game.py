import random
import time

from chess.board import ChessBoard


DEFAULT_BOARD = "rnbkqbnr pppppppp ........ ........ ........ ........ PPPPPPPP RNBKQBNR"


class ChessGame(object):
    """
    Class representing a chess game played from start to finish.
    :param player1/player2: Player objects
    :param verbosity: 0 for no print, 1 for just winner, 2 for normal board,
           or 2 to show possible moves
    :param board: starting board for the game
    :param first_move: player to go first, int 1 or 2 or default=random
    """
    def __init__(self, player1, player2, verbosity=1, pause=0,
                 first_move=None, board=DEFAULT_BOARD):
        self._player1 = player1
        self._player2 = player2
        self._verbosity = verbosity
        self._pause = pause

        if first_move is None:
            self._first_move = random.randint(1, 2)
        else:
            assert first_move in (1, 2), "first_move must be int 1 or 2"
            self._first_move = first_move

        self._board = ChessBoard(str(self._first_move) + " " + board)

    def __str__(self):
        return "Player1: {}\nPlayer2: {}\n{}".format(self._player1, self._player2, self._board)

    @property
    def player1(self):
        """Returns player object set to player1."""
        return self._player1

    @property
    def player2(self):
        """Returns player object set to player2."""
        return self._player2

    @property
    def players(self):
        """Returns a tuple of (player1, player2) objects."""
        return self._player1, self._player2

    @property
    def board(self):
        """Returns current chess board"""
        return self._board

    @property
    def p1_pieces(self):
        return self._board.get_pieces(player=1)

    @property
    def p2_pieces(self):
        return self._board.get_pieces(player=2)

    @property
    def pieces(self):
        return self._board.get_pieces()

    @property
    def possible_moves(self):
        return self._board.calc_possible_moves()

    def get_other_player(self, player):
        """
        Returns the opposite player.
        :param player: a player object that is in the current game.
        """
        assert player in (self._player1, self._player2)
        if player == self._player1:
            return self._player2
        else:
            return self._player1

    def do_move(self, move):
        self._board = self._board.do_move(move)

    def play(self):
        """
        Plays a complete chess game from given board until the game ends.
        :returns result dict including 'winner', 'turns', 'final board'
        """
        board = self._board
        turn_number = 0
        while True:
            turn_number += 1
            if self._verbosity > 1:
                print(board)

            # sets player to current player's turn
            assert board.get_player_turn() in ("1", "2")
            if board.get_player_turn() == "1":
                player = self._player1
            else:
                player = self._player2

            # determine possible moves
            possible_moves = board.calc_possible_moves()
            if self._verbosity == 2:
                print("{} moves: {}".format(player, possible_moves))

            is_in_check = board.is_attacking_king(flip_player=True)

            # if no possible moves, game is over
            if len(possible_moves) == 0:
                # Game is over
                if is_in_check:
                    if self._verbosity > 0:
                        print("{} was checkmated in {} moves!".format(player,
                                                               turn_number))
                    winner = self.get_other_player(player)
                else:
                    if self._verbosity > 1:
                        print("There was a draw!")
                    winner = None
                break
            else:
                if is_in_check and self._verbosity > 1:
                    print("{} is in check".format(player))

            board = board.do_move(player.choose_move(board))
            time.sleep(self._pause)

        result = {"winner": winner,
                  "turns": turn_number,
                  "final board": board}

        return result

