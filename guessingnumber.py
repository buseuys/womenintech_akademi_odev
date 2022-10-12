#Number guessing game in Python 

from random import randint

def guess(number):
    user_number = int(input("Guess a number between 1 and 100"))
    while number != user_number:
        if number < user_number:
            print("Sorry, You Guessed too high! ")
        else:
            print("Sorry, You guessed too small!")
        user_number = int(input("Please try again! "))
    else:
        print("Hurray! You won!")

guess(randint(1, 100))

