# MrJ
# 10/18/2023
# Purpose: To create a premium gambling experience

import random

# Variables
bet = 0

dice1 = 0

dice2 = 0

count = 0

play_again = "y"

# Get User Bet
bet = int(input("How much would you like to bet?"))

dollars = bet

while play_again == "y":
    # Generate two random dice rolls
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = (dice1 + dice2)
    print(f"You rolled a {dice_sum}!")

    # If dice roll is 7, pay the patron $4 USD
    if dice_sum == 7:
        dollars += 4
        print("You won!")
    # If dice roll is anything else, collect $ 1 USD
    else:
        dollars -= 1
        print("So close.")

    if dollars > 0:
        print(f"Your current standing: ${dollars}")
    else:
        print("Out of money.")
        break

    play_again = input("Would you like to play again? (y/n)")
    print()

# Once they have decided it is, in fact, time to fold 'em
# Tell them what they've won Bob

if dollars > bet:
    print(f"Profits: {dollars-bet}")
    print("You're the best around, no one's gonna ever bring you down!")
elif dollars == bet:
    print(f"Profits: {dollars-bet}")
    print("You broke even, you lucky dog!")
elif dollars < bet:
    print(f"Profits: {dollars-bet}")
    print("You didn't win :(")
else:
    print("This is Sparta!")

    
