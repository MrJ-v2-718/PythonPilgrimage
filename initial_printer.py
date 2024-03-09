# MrJ
# 1/30/24
# Purpose: Get user's name, print their initials

def main():
    # Variables
    name = input("Enter your name - first, middle, last: ")

    tokens = name.split()

    # Use if statement to find initials
    if len(tokens) == 2:
        print(f"{tokens[1]}, {tokens[0][0]}")

    if len(tokens) == 3:
        # Last, F.L.
        print(f"{tokens[2]}, {tokens[0][0]}. {tokens[1][0]}.")
        
# CALL MAIN CALL MAIN CALL MAIN CALL MAIN
main()
    
