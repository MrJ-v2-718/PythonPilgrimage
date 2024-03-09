# MrJ
# Purpose: Get Input From User, Calc Average, And Find Smalles And Largest

def main():
    # Variables
    average = 0.0
    minimum = 0
    maximum = 0

    # List With User Input
    number = [0,0,0,0]

    for i in range(4):
        number[i] = int(input("Enter a number: "))

    average, minimum, maximum = calcStats(number)
    
    stupidPrintResults(average, minimum, maximum)
    

def calcStats(number):
    # Calc average, find smallest, and largest
    average = sum(number)/len(number)
    minimum = min(number)
    maximum = max(number)

    return average, minimum, maximum

def stupidPrintResults(average, minimum, maximum):
    print(f"Your average is {average}, your minimum is {minimum}, and your maximum is {maximum}.")

    

main()

