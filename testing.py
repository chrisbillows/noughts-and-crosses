import time
from my_funcs import *
import sys
import tty
import termios
import select
import os
from playsound import playsound



                

def print_win():
    end_time = time.time() + 3 # 5 seconds from now
    playsound("sounds/win-sfx-38507.mp3")
    while time.time() < end_time:
        print("YOU WIN! ", end=" ", flush=True)
        time.sleep(0.009) 
                                       
def print_win_keyboard_interupt():
    end_time = time.time() + 10 # 5 seconds from now
    old_settings = termios.tcgetattr(sys.stdin) # get the current terminal settings
    tty.setcbreak(sys.stdin.fileno()) # set the terminal to cbreak mode
    try:
        while time.time() < end_time:
            print("YOU WIN! ", end=" ", flush=True)
            time.sleep(0.009) # delay to slow down printing
            if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
                break # terminate the loop if any key is pressed
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings) # restore the original terminal settings

def play_sound():
    print(winner_msg)
    print(winner_face)
    playsound("sounds/win-sfx-38507.mp3", block=True)



active_player = ('user', 'o')
active_player2 = ('computer', 'o')


def winner_symbol_animation(active_player):
    if active_player[1] == 'x':
        winner_ascii = x_winner
    else:
        winner_ascii = o_winner

    count = 3
    while count > 0:
        print(winner_ascii, end="", flush=True)
        os.system('afplay /System/Library/Sounds/Submarine.aiff')
        count -=1
    print(f'{"*" * 21}\n** Three in a row! **\n{"*" * 21}\n\n\n') 


def end_game_msg(active_player):
    if active_player[0] == 'user':
        print(user_winner_msg)
        print(user_winner_face)
        playsound("sounds/win-sfx-38507.mp3")
    else:
        print(user_loser_msg)
        print(user_loser_face)
        playsound("sounds/game-over-38511.mp3")
        
 
print(winner_symbol_animation(active_player))
print(end_game_msg(active_player))
