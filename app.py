from my_funcs import *


clear_console()
welcome()

user_symbol, computer_symbol = decide_symbols()
active_player, inactive_player = randomise_first_to_play(user_symbol, computer_symbol)

board = init_board()
display_board(board)

moves = 4

while moves > 0:
    display_board(board)
    
    if active_player[0] == 'user': 
        human_move(board, user_symbol)
    else: 
        computer_move(board, computer_symbol)
    
    display_board(board)
    
    if check_for_winner(board) == True:
        winner_symbol_animation(active_player)
        end_game_msg(active_player)
        # print(f"{active_player[0].upper()} is the winner!")
        break

    moves -= 1
    active_player, inactive_player = inactive_player, active_player


print("\n\nThanks for playing!")
