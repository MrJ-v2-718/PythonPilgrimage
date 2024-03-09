# Purpose: Prompt user to enter 2 primary colors and display resulting color
# If not a primary color then print error message

# Variables
color1 = ""
color2 = ""
mixed = ""

# Instructions
print("Enter two primary colors to mix!")

# User Input
color1 = input("Enter your first color: ").lower()
color2 = input("Enter your second color: ").lower()

# If Statements
if color1 == "red":
    if color2 == "blue":
        mixed = "purple"
    else:
        mixed = "orange"
if color1 == "blue":
    if color2 == "red":
        mixed = "purple"
    else:
        mixed = "green"
if color1 == "yellow":
    if color2 == "red":
        mixed = "orange"
    else:
        mixed = "green"
else:
    print("That is not a primary color")

if mixed == "":
    print("You shouldn't be here")
        
print(f"Your intermediate color is...{mixed}!")
