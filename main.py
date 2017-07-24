import time

from board import ChessBoard


player_won = False
computer_won = False

board = ChessBoard("p krb.q.n. .......p ........ ........ ........ ........ PPPPPPPP ...K....")

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

# Play game
while True:
    print(board)
    if board.is_player_turn():
        possible_moves = board.calc_possible_moves()
        print("player moves: {}".format(possible_moves))

        is_in_check = board.is_attacking_king(flip_player=True)

        # if no possible moves, game is over
        if len(possible_moves) == 0:
            if is_in_check:
                # player lost
                print("Check mate")
                computer_won = True
            else:
                # this is a draw
                print("Game ends in a draw")
            break
        else:
            if is_in_check:
                print("Player 1 is in check")

        player_choice = input("choose your move: ")

        if player_choice in possible_moves:
            board = board.do_move(player_choice)
        else:
            print("Error cant make that move")
            time.sleep(2)
            continue
    else:
        # computer's turn
        possible_moves = board.calc_possible_moves()
        print("computer moves: {}".format(possible_moves))

        is_in_check = board.is_attacking_king(flip_player=True)

        # if no possible moves, game is over
        if len(possible_moves) == 0:
            if is_in_check:
                # computer lost
                print("Check mate")
                player_won = True
            else:
                # this is a draw
                print("Game ends in a draw")
            break
        else:
            if is_in_check:
                print("Player 2 is in check")

        computer_choice = board.best_move(possible_moves)
        board = board.do_move(computer_choice)


if player_won:
    print("Congrats you beat the unbeatable AI!")
elif computer_won:
    print("The unbeatable computer keeps his title.")
else:
    print("Game ended in a draw.")