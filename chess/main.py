import player

# required to make imports work properly
import sys
sys.path.append("../")
from game import ChessGame


def main():
    play_game()


def play_game():
    player1 = player.RandomComputer()
    player2 = player.OldMinimax()
    game = ChessGame(player1, player2, verbosity=2, first_move=1)
    #print(game.board)
    print(game)
    game.do_move("a2 a3")
    print(game)
    print()
    print(game.board)


if __name__ == "__main__":
    main()