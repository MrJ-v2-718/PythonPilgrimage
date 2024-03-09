# MrJ
# 1/30/24
# Purpose: Use 3 functions to create a guessing game.

import random
correct_response = ["You got it!","Wow! I'm totally impressed by your intellectual prowess!"]
incorrect_response = ["I've seen better tries :p", "That was pretty bad lol"]

def main():
    # Variables
    user_choice = 0
    computer_choice = 0
    keep_playing = "y"
    winner = ""

    while keep_playing == "y":
        user_choice = guess()
        computer_choice = random_number()
        winner = find_winner(user_choice, computer_choice)
        print_results(user_choice, computer_choice, winner)

        keep_playing = input("Play again! (y/n) ")
        

def guess():
    # Print instructions
    print("Guess a number 1 - 10")
    user = int(input("Enter a number: "))

    return user


def random_number():
    comp = random.randint(1, 10)
    return comp

def find_winner(user, comp):
    if user == comp:
        winner = "You Are Correct"
    elif user != comp:
        winner = "You Are Incorrect"
    else:
        print("Error")

    return winner

def print_results(user, computer, winner):
    print(f"         You chose: {user}")
    print(f"The computer chose: {computer}")
    print(winner)

    if winner == "You Are Correct":
        print(random.choice(correct_response))
    elif winner == "You Are Incorrect":
        print(random.choice(incorrect_response))
    else:
        print("Get out of here you troublemaker!")

main()


    
