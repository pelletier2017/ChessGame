import player

# required to make imports work properly
import sys
sys.path.append("../")
from tournament import ChessTournament
from game import ChessGame


def main():
    #play_tournament()
    play_game()


def play_tournament():
    player1 = player.RandomComputer("random ai")
    player2 = player.MinimaxComputer("less dumb ai")
    result = ChessTournament(player1, player2, 10).play_games()
    print(result)


def play_game():
    player1 = player.RandomComputer("random ai")
    player2 = player.MinimaxComputer("less dumb ai")
    game = ChessGame(player1, player2, verbosity=2, pause=0.25)
    game.play()

if __name__ == "__main__":
    main()
