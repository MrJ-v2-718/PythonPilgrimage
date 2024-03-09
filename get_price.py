# MrJ
# 8/28/23
# Purpose: Get price of 3 items with tax. Sales tax is 6%

# Variables
items = [0.0,0.0,0.0]
subtotal = 0.0
total = 0.0
tax = 0.0

# User Input
items[0] = float(input("Enter the price of your first item: "))
items[1] = float(input("Enter the price of your second item: "))
items[2] = float(input("Enter the price of your third item: "))
print()

subtotal = sum(items)
tax = subtotal * 0.06
total = subtotal + tax

# Print the Results
#print("Your subtotal is",subtotal,"dollars, the taxes is",tax,"dollars, and your total is",total,"dollars.")
print(f'Subtotal: ${subtotal:,.2f}')
print(f'     Tax: ${tax:,.2f}')
print(f'   Total: ${total:,.2f}')
