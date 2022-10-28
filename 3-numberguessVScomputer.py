#Number guessing game VS computer

import random

def computer_guess(x):
    start = 1
    end = 100
    result = ""

    while result != "t":
        guess = random.randint(start, end)
        result = input(f"if {guess} value is bigger than your number press (h); otherwise, press (s). It it matches your number, press (t)").lower()
        if result == "h":
            end = guess - 1
        elif result == "s":
            start = guess + 1
            
    print("Hurray! You won!")
    
computer_guess(19)

