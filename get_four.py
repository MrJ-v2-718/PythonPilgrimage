# MrJ
# 8/30/2023
# Purpose: Given 4 numbers, use string formatting expressions to find the avg
#          & product as integers, then as a float

# Variables
num = [0.0,0.0,0.0,0.0]
product = 0.0
avg = 0.0

# Get User Input
num[0] = float(input("Enter a number: "))
num[1] = float(input("Enter a number: "))
num[2] = float(input("Enter a number: "))
num[3] = float(input("Enter a number: "))

# Calc the product and average
product = num[0] * num[1] * num[2] * num[3]
avg = sum(num) / 4

# Print the results as integers
print(f"The product of the numbers is:  { product:.0f}")
print(f"The average of the numbers is:  { avg:.0f}")

print(f"The product of the numbers is:  { product:.2f}")
print(f"The average of the numbers is:  { avg:.2f}")
