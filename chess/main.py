import player

# required to make imports work properly
import sys
sys.path.append("../")
from game import ChessGame


def main():
    play_game()


def play_game():
    p1 = player.RandomComputer()
    p2 = player.BasicMinimax()
    game = ChessGame(p1, p2)
    game.play()



if __name__ == "__main__":
    main()