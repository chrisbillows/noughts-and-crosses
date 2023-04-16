import readchar
from time import sleep

def press_x_or_o():
    print("SELECT o OR x")
    user_symbol = None

    while True:
        key = readchar.readkey().lower()
        if key == "o" or key == "x":
            user_symbol = key
            break
        else:
            print("INVALID INPUT. PLEASE SELECT o OR x")

    print(f"GREAT. YOU HAVE SELECTED {user_symbol.upper()}")

def press_any_key():
    print("\n\nOkay, LET'S GO!\n\nPress any key to start the game!")
    key = readchar.readkey().lower()
    # while key == '':
    #     print("not pressed yet")
    #     sleep(0.2)    
    return type(key)

    # while True:
    #     key = readchar.readkey().lower()
    #     if key == "o" or key == "x":
    #         user_symbol = key
    #         break
    #     else:
    #         print("INVALID INPUT. PLEASE SELECT o OR x")

    # print(f"GREAT. YOU HAVE SELECTED {user_symbol.upper()}")

# my_str = press_any_key()

# if my_str != '':
#     print("STRING")
# else:
#     print("TWAT")
print(press_any_key())



