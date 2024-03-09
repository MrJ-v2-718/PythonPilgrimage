# Prompt user to enter two primary colors, display mixed value

def main():
    # Variables
    color1 = ""
    color2 = ""
    keep_playing = "y"
    mixed = ""

    while keep_playing == "y":
        # Get Input function
        color1, color2 = get_input()
        #Mix Colors function
        mixed = mix_colors(color1, color2, mixed)
        # Print Results function
        print_results(mixed)

        keep_playing = input("Would you like to play again? ").lower()
        print()
    print("Thanks for playing.")


def get_input():
    # Instructions
    print("Enter two different primary colors to mix.")

    # Get User Input
    color1 = input("First color: ")
    color2 = input("Second color: ")

    return color1.lower(), color2.lower()

def mix_colors(color1, color2, mixed):
    # if statements for mixing colors
    if color1 == "red":
        if color2 == "blue":
            mixed = "purple"
        else:
            mixed = "orange"
    elif color1 == "blue":
        if color2 == "red":
            mixed = "purple"
        else:
            mixed = "green"
    elif color1 == "yellws":
        if color2 == "red":
            mixed = "orange"
        else:
            mixed = "green"
    else:
        print("You did not enter a primary color, don't do that.")

    return mixed

def print_results(mix):
    if mix != "":
        print(f"Those colors make...{mix}.")

main()
    









        
    
