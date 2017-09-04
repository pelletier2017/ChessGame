import player

# required to make imports work properly
import sys
sys.path.append("../")
from game import ChessGame


def main():
    play_game()
    #test_minimax()


def play_game():
    player1 = player.RandomComputer("random ai")
    player2 = player.OldMinimax("less dumb ai")
    game = ChessGame(player1, player2, verbosity=2, pause=0)
    game.play()


def test_minimax():
    player1 = player.OldMinimax("old minimax")
    player2 = player.BasicMinimax("newer minimax")
    game = ChessGame(player1, player2, verbosity=2, pause=0)
    game.play()



if __name__ == "__main__":
    main()
