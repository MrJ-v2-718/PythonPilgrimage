# Brandon Jones
# 1/23/2024
# Purpose: Asks the user to enter a series of positive numbers and enter a negative 
# number to signal the end of the series. After all positive numbers have been 
# entered, the program should display the sum of the positve integers.

def main():
    # Variables
    positive_nums = []
    positive_sum = 0
    num_entered = 0
    print()
    print("Welcome to the sum calculator.")
    print()
    print("You will enter positive numbers to sum, when finished enter a negative.")
    print()

    # A while loop that iterates as long as the number entered is positve.
    while num_entered >= 0:
        raw_input = ""
        raw_input = input("Please enter a number: ")
        
        # Here we ensure user input is an integer before we cast it as such.
        try:
            num_entered = int(raw_input)
        except ValueError:
            # If the value is not a number, the loop starts over from the beginning.
            print("That is not a number. Please try again.")
            continue
        
        if num_entered >= 0:
            # If positive, we want to add it to the list of positive numbers
            positive_nums.append(num_entered)
        elif num_entered < 0:
            # If negative, we want to exit the loop. This is a failsafe since the while loop
            # already checks for positve, but ensures that an error is avoided.
            break
        else:
            # This will print if the input doesn't match the criteria above and shouldn't execute.
            print("Error")

    # A for loop to sum the contents of the positve number list.
    for i in positive_nums:
        positive_sum += i

    # Displays the sum to the user.
    print(f"The sum of your numbers is {positive_sum}.")

# Always call your functions, not doing so will prevent the program from executing.
main()
