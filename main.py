import player
from game import ChessGame


def main():
    player1 = player.Computer("fake Andrew")
    player2 = player.Computer("random ai")
    game = ChessGame(player1, player2)
    game.play()


if __name__ == "__main__":
    main()

    # interesting start
    #board = ChessBoard("p krb.q.n. .......p ........ ........ ........ ........ PPPPPPPP ...K....")

    # rook able to kill pawn attacking king without forcing king to move
    #board = ChessBoard("p .rb.q.n. .......p ........ r....... .k...... P....... .PPPPPPP ...K....")

    # player is getting checkmated
    #board = ChessBoard("p k....... .Q...... ..B..... ........ ........ ........ ........ ...K....")

    # player is getting checked
    #board = ChessBoard("p k....... .Q...... ........ ........ ........ ........ ........ ...K....")

    # computer is getting checkmated
    #board = ChessBoard("c K....... .q...... ..b..... ........ ........ ........ ........ ...k....")

    # computer is getting checked
    #board = ChessBoard("c K....... .q...... ........ ........ ........ ........ ........ ...k....")