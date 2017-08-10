import player

# required to make imports work properly
import sys
sys.path.append("../")
from tournament import ChessTournament


def main():
    player1 = player.RandomComputer("random ai")
    player2 = player.MinimaxComputer("less dumb ai")
    result = ChessTournament(player1, player2, 10).play_games()
    print(result)

if __name__ == "__main__":
    main()
