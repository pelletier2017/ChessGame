import time

from board import ChessBoard


# TODO

# class restructure: player class, computer class, chess_game, etc


# check_mate check (implement board.is_square_threatened
# en passe
# castle
# when you move piece and your king is able to be attacked


# edge cases to test:
# kings helping with check-mate
# castle body block2v


player_won = False
computer_won = False

board = ChessBoard("p krb.q.n. .......p ........ ........ ........ ........ PPPPPPPP ...K....")
# Play game
while True:
    print(board)
    if board.is_player_turn():
        possible_moves = board.calc_possible_moves()
        print("player moves: {}".format(possible_moves))

        player_choice = input("choose your move: ")

        if len(possible_moves) == 0:
            # this is a draw
            print("Player no moves")
            break
        if player_choice in possible_moves:
            board = board.do_move(player_choice)
        else:
            print("Error cant make that move")
            time.sleep(3)
            continue
    else:
        # computer's turn
        possible_moves = board.calc_possible_moves()
        print("computer moves: {}".format(possible_moves))

        if len(possible_moves) == 0:
            # this is a draw
            print("Computer no moves")
            break
        computer_choice = board.best_move(possible_moves)
        board = board.do_move(computer_choice)


if player_won:
    print("Congrats you beat the unbeatable AI!")
elif computer_won:
    print("The unbeatable computer keeps his title.")
else:
    print("Game ended in a draw.")