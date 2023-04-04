from my_funcs import *

clear_console()
welcome()

user_symbol, computer_symbol = decide_symbols()
first_player, second_player = randomise_first_to_play(user_symbol, computer_symbol)
active_player, inactive_player = first_player, second_player

board = init_board()
display_board(board)

moves = 4

while moves > 0:
    display_board(board)
    if active_player[0] == 'user':
        human_move(board, user_symbol)
    else:
        computer_move(board, computer_symbol)
    moves -= 1
    active_player, inactive_player = inactive_player, active_player
    display_board(board)

print("All moves played")
