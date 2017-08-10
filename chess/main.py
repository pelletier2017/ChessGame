import player

# required to make imports work properly
import sys
sys.path.append("../")

from game import ChessGame


def main():
    player1 = player.RandomComputer("fake Andrew", pause=0)
    player2 = player.MinimaxComputer("random ai", pause=0)
    game = ChessGame(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
