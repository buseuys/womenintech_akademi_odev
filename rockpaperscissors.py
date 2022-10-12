import random
player_score = computer_score = 0
computer_choice = 0

def print_result(winner = "Computer"):
    print(f"Computer's Choice: {computer_choice}\n\n Winner: {winner}")
    global player_score, computer_score

    if winner == "Computer":
        computer_score += 100
    else:
        player_score += 100

print("Rock Paper Scissors!\n" + "-"*37)

while True:
    print("\n1 - Rock\n2 - Paper \n3 - Scissors \n To finish the game give another value.")
    player_choice = int(input("Enter a choice: "))
    computer_choice = random.choice([1, 2, 3])   
    
    if player_choice == computer_choice:
        print("Both players selected, try again")
    elif player_choice == 1:
        if computer_choice == 2:
            print_result("Paper covers rock! You lose :(")
        elif computer_choice == 3:
            print_result("Rock smashes scissors! You win!")
    elif player_choice == 2:
        if computer_choice == 1:
            print_result("Paper covers rock! You win!")
        elif computer_choice == 3:
            print_result("Scissors cuts paper! You lose :(")
    elif player_choice == 3:
        if computer_choice == 1:
            print_result("Rock smashes scissors! You lose :(")
        elif computer_choice == 2:
            print_result("Scissors cuts paper! You win!")
    else:
        break
    
print(f"\n\n Your score {player_score} - Computer's score {computer_score}")
if player_score > computer_score: print("You won!")
elif player_score < computer_score: print("You lost :( ")
else: print("It's a tie!")
