# MrJ
# 1/16/24
# Purpose: Write a Python program that uses a while loop to simulate a simple coundown.

# The program should prompt the user to enter a positive integer,
#    and then count down from that number to 1, printing each step.

# Should also ask for new number if negative number is entered

# Variables
positive_integer = int(input("Please enter a positive integer: "))

if positive_integer <= 0:
    positive_integer = int(input("Please enter a positive integer"))

for i in range(positive_integer, 0, -1):
    print(i)
