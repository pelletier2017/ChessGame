from board import ChessBoard

# working on getting possible_moves into main

player_won = False
computer_won = False

board = ChessBoard("p k....... .......p ........ ........ ........ ........ PPPPPPPP ...K....")
# Play game
while True:
    print(board)
    if board.is_player_turn():
        # ask player for his turn
        player_choice = input("choose your move: ")
        possible_moves = board.calc_possible_moves()
        if len(possible_moves) == 0:
            # draw
            print("Player no moves")
            break
        if player_choice in possible_moves:
            board = board.do_move(player_choice)
        else:
            # ask player for input again
            continue
    else:
        # computer's turn
        possible_moves = board.calc_possible_moves()
        if len(possible_moves) == 0:
            # draw
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