from playsound import playsound
import readchar
from my_funcs import wait_for_any_key, wait_for_h_or_t

import os
import platform
from random import choice, randint
from time import sleep
from graphics import *

def coin_toss():
    for i in range(15):
        sleep(0.2)
        coin_toss = choice([' H ', ' T '])
        print(coin_toss, end='', flush=True)
        # os.system('afplay /System/Library/Sounds/Ping.aiff')
    sleep(0.01)
    print()
    return coin_toss


def game_start():
    print("\n\nOkay, LET'S GO!\n\nPress any key to start the game!")
    wait_for_any_key()
    playsound("sounds/321-go.mp3")



def randomise_first_to_play(user_symbol, computer_symbol):
    coin_dict = {'h':'heads', 't':'tails'}
    print("\nLets see who goes first!\n\nPick h for heads or t for tails: " )  # ...\n\n" + 46 *"-")
    user_coin = coin_dict[wait_for_h_or_t()]
    print(f"\n\nYou selected {user_coin.upper()}. \n\nGOOD LUCK!\n")
       
    coin_winner = coin_dict[coin_toss().strip().lower()]

    if user_coin == coin_winner:
        print("f\nYES! {user_coin} wins!")
        player1 = 'user'
        player2 = 'computer'
    else:
        print(f"\nOh no! {user_coin} loses!")
        player1 = 'computer'
        player2 = 'user'                

    print(f"\nSo going first will be:  {player1.upper()}")
    print(f"And going second will be:  {player2.upper()}")
    os.system('afplay /System/Library/Sounds/Ping.aiff')
    
    sleep(1)
    
    if player1 == 'user':
        return ('user', user_symbol), ('computer', computer_symbol)
    else:
        return ('computer', computer_symbol), ('user', user_symbol)


user_symbol = 'o'
computer_symbol = 'x'

active_player, inactive_player = randomise_first_to_play(user_symbol, computer_symbol)

game_start()

#print(coin_toss())
