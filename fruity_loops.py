# MrJ
# Fruity Loops

import random

# Variables
guess = 0
randomNumber = 0
numberGuesses = 0
keep_playing = "y"

# give user info, get their guess
print("Guess a number 1-20")
keep_playing = input("Do you want to play a game? (y/n)")

# generate random number
randomNumber = random.randint(1,20)

while keep_playing == "y":
    guess = int(input("What number do you guess?"))
    if randomNumber == guess:
        print("You guessed it!")
        keep_playing = input("Do you want to play again? (y/n)")
        if keep_playing == "y":
            randomNumber = random.randint(1,20)
            numberGuesses = 0
    elif guess < randomNumber:
        print("Guess is too low")
        keep_playing = input("Do you want to play again? (y/n)")
    else:
        print("Guess is too high")
        keep_playing = input("Do you want to play again? (y/n)")
    numGuess += 1

# end of game feedback
if numberGuesses <= 5:
    print(f"Great job, you got it in {numberGuesses} tries")
else:
    print(f"Not so great, you got it in {numberGuesses} tries")

