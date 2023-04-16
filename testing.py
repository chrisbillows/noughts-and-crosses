import readchar

def wait_for_x_or_o():
    while True:
        key = readchar.readkey().lower()
        if key == "o" or key == "x":
            user_symbol = key
            return key
        else:
            print("\n------INVALID INPUT------\n\nPlease press either'o' or 'x': ")
  

def decide_symbols():
    symbols = ['x', 'o']
    print("Do you want to be noughts or crosses (o or x): ")
    user_symbol = wait_for_x_or_o()
        
    symbols.remove(user_symbol)
    computer_symbol = symbols[0]

    print("\n", 46 * "-")
    print(f"\nGreat! You will play as {user_symbol}'s.")
    print(f"\nI will play as {computer_symbol}'s.\n")

    return user_symbol, computer_symbol



user_symbol, computer_symbol = decide_symbols()

print(user_symbol)
