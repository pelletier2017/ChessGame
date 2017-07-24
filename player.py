import random
import time


class Player:
    def __init__(self, name):
        self._name = name
        self._games_won = 0

    def __str__(self):
        return self._name

    def increment_score(self):
        self._games_won += 1


class Computer(Player):
    def choose_move(self, board, possible_moves):
        random_move = random.randrange(len(possible_moves))
        time.sleep(0.5)
        return possible_moves[random_move]


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