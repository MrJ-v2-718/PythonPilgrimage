#MrJ
#Purpose: User enters number of bagels they want to buy. If less than 6,
#25% off. If between 6 and 12, then 40% off. More than 12, 50% off.

#Variables
number_bagels = 0
price = 4.99
total = 0.0

#User Input
number_bagels = int(input("How many bagels would you like customer?"))

#Processing
if(number_bagels < 6):
    total = (price * .75) * number_bagels
    print(f"You saved 25% on your bagels today and your total is ${total:.2f}.")
elif (6 <= number_bagels <= 12):
    total = (price * .6) * number_bagels
    print(f"You saved 40% on your bagels today and your total is ${total:.2f}.")
elif (number_bagels > 12):
    total = (price * .5) * number_bagels
    print(f"You saved 50% on your bagels today and your total is ${total:.2f}.")
