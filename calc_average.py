# MrJ
# 1/23/24
# Purpose: Get 4 numbers from user, calc average, max, and min

def main():
    # Variables
    num1 = 0.0
    num2 = 0.0
    num3 = 0.0
    num4 = 0.0

    # Get input
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter a number: "))
    num3 = float(input("Enter a number: "))
    num4 = float(input("Enter a number: "))

    # Create a function to calculate stuff
    average, minimum, maximum = calc_stats(num1, num2, num3, num4)

    # Print calculated numbers
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

def calc_stats(num1, num2, num3, num4):
    # Create list
    num_list = [num1, num2, num3, num4]
    
    # Average
    average = sum(num_list) / len(num_list)
    
    # Minimum
    minimum = min(num_list)
    
    # Maximum
    maximum = max(num_list)

    return average, minimum, maximum


main()
