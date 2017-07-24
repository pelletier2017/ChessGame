
# user picks the choice
player_choice = input("choose your move: ")

while player_choice not in possible_moves:
    print("Error cant make that move")
    time.sleep(2)
    player_choice = input("choose your move: ")

board = board.do_move(player_choice)

# in check message
print("Player 1 is in check")

# draw message
print("Game ended in a draw.")

# check mated message
print("Checkmate. You LOSE!")
print("The unbeatable computer keeps his title.")

# enemy check mated
print("Checkmate. You WIN!")
print("Congrats you beat the unbeatable AI!")
