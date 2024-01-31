# MrJ
# 1/30/2024
# Purpose: Develop a program designed for children. The program will show 2 to 4 coins.
# The coins can be a quarter, dime, nickel, or penny. The user will then add up their coins
# and enter their number. The program should notify them if they are correct or not. If the
# users answer is incorrect, they should be shown the addition problem. For example,
# two pennies would output: 1 + 1 = 2. The program should continue until the user stops it.
# I have not copied the following code from anyone or from any website.
import random

# The purpose of the main function is to call the other functions, aka "The Play Button."
# Reference later to determine if last in a sequence.
num_coins = random.randint(2, 4)
def main():
    keep_playing = "y"
    
    while keep_playing != "n":
        # The main game loop.
        print()
        print(f"          Welcome to Pocket Change!")
        print(f"Can you do math? Let's find out together!")
        print()
        gen_quarters, gen_dimes, gen_nickels, gen_pennies, gen_total = generate_coins()
        print(f"You have {gen_quarters} quarter(s), {gen_dimes} dime(s), {gen_nickels} nickel(s), and {gen_pennies} penn(y/ies).")
        user_total = input("Please enter your guess as to how much pocket change you have (e.g. $0.20): $")
        
        try:
            user_total = float(user_total)
        except ValueError:
            # If the value is not a number, the loop starts over from the beginning.
            print("That is not the correct format. Please try again.")
            continue
        compare_totals(user_total, gen_quarters, gen_dimes, gen_nickels, gen_pennies, gen_total)
        # Be sure to prevent infinite loops by providing exits for the user.
        keep_playing = input("Would you like to play again? (y/n) ")
    

# The purpose of the generate_coins() function is to generate 2 to 4 US currency coins.
def generate_coins():
    # Initialize the variables that will be used in this function.
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    total = 0.0

    # A for loop that loops generates between two and four US currency coins.    
    for n in range(num_coins):
        coin_gen = random.randint(1, 4)
        if coin_gen == 1:
            quarters += 1
        elif coin_gen == 2:
            dimes += 1
        elif coin_gen == 3:
            nickels += 1
        elif coin_gen == 4:
            pennies += 1
        else:
            # Shouldn't execute.
            print("Error")
            
    # Tally all the coins that were generated during the for loop.
    total += quarters * 0.25
    total += dimes * 0.10
    total += nickels * 0.05
    total += pennies * 0.01
    total = round(total, 2)

    # We need to return the total and reassign it a value in the main function.
    return quarters, dimes, nickels, pennies, total
        
    
# The purpose of compare_totals is to compare user input with the correct answer and give feedback.
def compare_totals(sent_user_total, sent_gen_quarters, sent_gen_dimes, sent_gen_nickels, sent_gen_pennies, sent_gen_total):
    # Allows the alteration of num_coins without changing a global variable
    countdown = num_coins
    print()
    # If the entered answer is correct:
    if sent_user_total == sent_gen_total:
        praise = random.randint(1, 3)

        # Praise that varies to keep the user motivated to keep doing math.
        if praise == 1:
            print("Great job, you can do math!")
        elif praise == 2:
            print("Yay, you're mathing so hard right now!")
        elif praise == 3:
            print("Congratulations, you got it!")

    # *NEEDS SOME WORK* If the entered answer is wrong: *NEEDS SOME WORK*
    elif sent_user_total != sent_gen_total:
        print("Sorry, wrong answer.")
        
        if sent_gen_quarters != 0:
            for quarter in range(sent_gen_quarters):
                print(25, end = " ")
                
                if countdown == 1:
                    break
                 
                if sent_gen_quarters != 0:
                    print(" + ", end = " ")
                    sent_gen_quarters -= 1
                    countdown -= 1
                else:
                    break
            
        if sent_gen_dimes != 0:
            for dime in range(sent_gen_dimes):
                print(10, end = " ")
                
                if countdown == 1:
                    break
                 
                if sent_gen_dimes != 0:
                    print(" + ", end = " ")
                    sent_gen_dimes -= 1
                    countdown -= 1
                else:
                    break

        if sent_gen_nickels != 0:
            for nickel in range(sent_gen_nickels):
                print(5, end = " ")
                
                if countdown == 1:
                    break
                 
                if sent_gen_nickels != 0:
                    print(" + ", end = " ")
                    sent_gen_nickels -= 1
                    countdown -= 1
                else:
                    break
          
        if sent_gen_pennies != 0:
            for penny in range(sent_gen_pennies):
                print(1, end = " ")
                
                if countdown == 1:
                    break

                if sent_gen_pennies != 0:
                    print(" + ", end = " ")
                    countdown -= 1
                    sent_gen_pennies -= 1
                else:
                    break

        print(f"= ${sent_gen_total:.2f}")
        
# Always call main or your program will not execute
main()
