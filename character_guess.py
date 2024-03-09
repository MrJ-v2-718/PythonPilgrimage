# MrJ

import random
import string

# Variables
bet = 0

letter = ""

count = 0

play_again = "y"

# Get User Bet
bet = int(input("How much would you like to bet?"))

dollars = bet

while play_again == "y":
    # Find Random Letter
    letter = random.choice(string.ascii_letters)
    print(letter)

    guess = input("Enter a single character:")
    print()

    if guess == letter:
        dollars += 10
        print("Correct!")
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

    
