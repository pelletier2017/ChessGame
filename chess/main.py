import chess.player
from chess.game import ChessGame


def main():
    player1 = player.Computer("fake Andrew")
    player2 = player.Computer("random ai")
    game = ChessGame(player1, player2)
    game.play()


if __name__ == "__main__":
    main()
