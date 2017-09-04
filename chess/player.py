import math
import random
import time


class Player(object):
    def __init__(self, name="No Name"):
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self._name)


class RandomComputer(Player):
    def choose_move(self, board):
        """
        Chooses a random move out of possible_moves
        :param board: board object
        :param possible_moves: list of strings representing moves
        :return: string in form "a1 b2"
        """
        possible_moves = board.calc_possible_moves()
        return random.choice(possible_moves)


class OldMinimax(Player):
    @staticmethod
    def choose_move(board):
        """
        Chooses best move based on looking at list of moves and picking the best.
        :param board: board object
        :param possible_moves: list of strings representing moves
        :return: string in form "a1 b2"
        """
        possible_moves = board.calc_possible_moves()
        best_score = board.do_move(possible_moves[0]).evaluate() * -1
        best_moves = [possible_moves[0]]
        for possible_move in possible_moves:
            score = board.do_move(possible_move).evaluate() * -1
            if score > best_score:
                best_score = score
                best_moves = [possible_move]
            if score == best_score:
                best_moves.append(possible_move)

        random_move = random.randrange(len(best_moves))

        return best_moves[random_move]

        # alpha is the best value for the maximizer along the path to the root
        # beta is the best value for the minimizer along the path to the root

        # maximizer takes its children and passes back its max
        # before looking at each child it checks something with alpha/beta


class BasicMinimax(Player):
    def choose_move(self, board, depth=2):
        """
        Chooses best move based on looking at list of moves and picking the best.
        :param board: board object
        :param possible_moves: list of strings representing moves
        :return: string in form "a1 b2"
        """
        possible_moves = board.calc_possible_moves()
        move_score = {}
        for possible_move in possible_moves:
            new_board = board.do_move(possible_move)
            move_score[possible_move] = -self.negamax(new_board, depth-1)

        best_move = max(move_score, key=move_score.get)
        return best_move

    def negamax(self, board, depth):
        """
        Recursively finds the max score for a given board state. Relies on
        the formula max(a, b) = -min(-a, -b).
        :param board: board object
        :param depth: integer
        :return: integer for best score
        """
        # if it has reached max depth, it is a leaf node
        if depth == 0:
            return board.evaluate()

        possible_boards = board.get_possible_boards()
        # if it has no possible moves, it is a leaf node
        if len(possible_boards) == 0:
            return board.evaluate()

        max_score = -math.inf
        for board in possible_boards:
            score = -self.negamax(board, depth-1)
            if score > max_score:
                max_score = score
        return max_score


class Human(Player):
    @staticmethod
    def choose_move(board):
        """
        Asks the user for a move, if the move is not in the list of possible 
        moves then it asks the user for another move.
        :param board: board object
        :param possible_moves: list of strings representing moves
        :return: string in form "a1 b2"
        """
        possible_moves = board.calc_possible_moves()
        while True:
            player_choice = input("choose your move: ")
            if player_choice in possible_moves:
                break
            print("Error cant make that move")
            time.sleep(2)

        return player_choice
