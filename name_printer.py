# User enter full name, print out last name, first inital, and middle initial

def main():
    # Variables
    initials = ""
    full_name = ""
    name = ""
    name = []

    # User Input
    full_name = input("Enter your full name: ")

    name = full_name.split()

    print(name)

    for string in name:
        initials += (string[0].upper() + ". ")

    print(initials)

    change_format(name)

def change_format(name):
    # if two names X, X.
    if len(name) == 2:
        print("{}, {}.".format(name[1], name[0][0]))

    # if three names X, X. X.
    if len(name) == 3:
        print("{}, {}. {}. ".format(name[2], name[0][0], name[1][0]))

main()


