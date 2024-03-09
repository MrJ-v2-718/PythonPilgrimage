# MrJ
# Branching

#Variables
temp = 0

# User Input
print("What is the temperature? ")
temp = int(input("Enter here: "))

# Processing
if temp < 40:
    print("It's cold outside.")
elif temp >= 40 & temp <= 65:
    print("It's okay weather I guess.")
else:
    print("Nice weather we're having!")
