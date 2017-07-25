import random
import time


class Player:
    def __init__(self, name, pause=0.5):
        self._name = name
        self._pause = pause
        self._games_won = 0

    def __str__(self):
        return self._name

    def increment_score(self):
        self._games_won += 1


class RandomComputer(Player):
    def choose_move(self, board, possible_moves):
        random_move = random.randrange(len(possible_moves))
        time.sleep(self._pause)
        return possible_moves[random_move]


class MinimaxComputer(Player):
    def choose_move(self, board, possible_moves):
        best_score = board.do_move(possible_moves[0]).evaluate() * -1
        best_moves = [possible_moves[0]]
        for i in range(1, len(possible_moves)):
            score = board.do_move(possible_moves[i]).evaluate() * -1
            if score > best_score:
                best_score = score
                best_moves = [possible_moves[i]]
            if score == best_score:
                best_moves.append(possible_moves[i])

        random_move = random.randrange(len(best_moves))

        time.sleep(self._pause)
        return best_moves[random_move]


class Human(Player):
    def choose_move(self, board, possible_moves):
        player_choice = input("choose your move: ")

        while player_choice not in possible_moves:
            print("Error cant make that move")
            time.sleep(2)
            player_choice = input("choose your move: ")
        return player_choice




"""
board = board.do_move(player_choice)

# in check message
print("Player 1 is in check")

# draw message
print("Game ended in a draw.")

# check mated message
print("Checkmate. You LOSE!")
print("The unbeatable computer keeps his title.")

# enemy check mated
print("Checkmate. You WIN!")
print("Congrats you beat the unbeatable AI!")
"""