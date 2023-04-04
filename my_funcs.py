import os
import platform
from random import choice
from time import sleep

####################
#### GAME SET UP
####################

def init_board():
    board = ['-', '-', '-', '-'] 
    return board

def welcome():
    print("Lets play tic-tac-toe.\n")


def decide_symbols():
    symbols = ['x', 'o']
    user_symbol =  input("Do you want to be noughts or crosses (o or x): ")
    symbols.remove(user_symbol)
    computer_symbol = symbols[0]
    print(f"\nAnd I will play as {computer_symbol}'s.\n")
    return user_symbol, computer_symbol


def randomise_first_to_play(user_symbol, computer_symbol):
    print('Randomly picking who goes first...')
    players = ['user', 'computer']
    player1 = choice(players)
    players.remove(player1)
    player2 = players[0]

    print(f"Going first will be: {player1}")
    print(f"Going second will be: {player2}")

    if player1 == 'user':
        return (player1, user_symbol), (player2, computer_symbol)
    else:
        return (player1, computer_symbol), (player2, user_symbol)


####################
#### DISPLAYING BOARD
####################

def clear_console():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

def display_board(board):
    clear_console()
    print(f"  0    1    2    3\n{board}\n")


####################
#### MAKING MOVES
####################

def update_avail_moves(board):
    available_moves = []
    for idx, val in enumerate(board):
        if val == '-':
            available_moves.append(idx)
    return available_moves


def human_move(board, user_symbol):
    available_moves = update_avail_moves(board)
    display_available_moves = ', '.join([str(x) for x in available_moves])
    user_move = input(f"\nYour move...\nPick a position: ({display_available_moves}): ")
    board[int(user_move)] = user_symbol
    return board

def computer_move(board, computer_symbol):
    available_moves = update_avail_moves(board)
    computer_thinking_animation()
    computer_move = choice(available_moves)
    board[computer_move] = computer_symbol
    computer_move_animation(board, computer_move)    


def computer_thinking_animation():
    print("COMPUTER TO MOVE", end='')
    for i in range(5):
        sleep(0.2)
        print('.', end='', flush=True)
    sleep(0.2)
    print()


def computer_move_animation(board, computer_move):
    display_board(board) # Displays board showing computers move + below statement
    print(f"COMPUTER TAKES POSITION {computer_move}")
    os.system('afplay /System/Library/Sounds/Ping.aiff')
