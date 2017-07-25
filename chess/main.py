from chess import player
from chess.game import ChessGame


def main():
    player1 = player.RandomComputer("fake Andrew")
    player2 = player.MinimaxComputer("random ai")
    game = ChessGame(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
