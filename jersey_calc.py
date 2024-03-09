# MrJ
# 9/25/2023
# jersey_calc.py
# Purpose : To calculate the price of jerseys
# I did not copy this program from anyone else

# Variables
number_of_jerseys = 0
discount = 0.0
subtotal = 0.0
total = 0.0
price = 49.0

# User Input
number_of_jerseys = int(input("Please enter how many \
jerseys you would like to purchase: "))


# Processing
if number_of_jerseys < 10:
    discount = 0
elif 9 < number_of_jerseys < 20:
    discount = 0.05
elif 19 < number_of_jerseys < 50:
    discount = 0.08
elif 49 < number_of_jerseys < 100:
    discount = 0.1
elif number_of_jerseys > 99:
    discount = 0.15
else:
    discount = 0

subtotal = price * number_of_jerseys
calc_discount = subtotal * discount
total = subtotal - calc_discount


# Output
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${calc_discount:.2f}")
print(f"   Total: ${total:.2f}")
