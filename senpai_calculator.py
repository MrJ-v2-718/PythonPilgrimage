# MrJ
# Senpai Calculator
# Purpose: Calculates the oldest members of a group.

def main():
    # Initialization
    choice = 0

    while choice <= 3:
        # display menu
        menu()
        choice = int(input("\nEnter your menu choice: "))

        if choice == 1:
            addPerson()
        elif choice == 2:
            displayData()
        elif choice == 3:
            displayOldest()
        else:
            print("Have a nice day.")


def menu():
    print("MENU")
    print("1 - Add name and age to file")
    print("2 - Display all names and ages")
    print("3 - Display the oldest person")
    print("4 - Exit the program")


def addPerson():
    outfile = open("age.txt", "a")
    name = input("Enter name: ")
    age = input("Enter age: ")

    # Write name and age to file
    outfile.write(f"{name}\n")
    outfile.write(f"{age}\n")

    # Close the file
    outfile.close()
    print("Data added to the file.")


def displayData():
    # Variables
    name = ""
    age = ""

    # Open the file
    infile = open("age.txt", "r")

    # Reading the first name
    name = infile.readline()
    print("\nNAME \t AGE")

    # While loop to read until there's no data
    while name != "":
        # Get age
        age = infile.readline()
        # Remove new line
        name = name.rstrip("\n")
        age = age.rstrip("\n")

        # Print name and age
        print(f"{name} \t {age}")

        name = infile.readline()
    infile.close()


def displayOldest():
    infile = open("age.txt", "r")
    # Read first name
    name = infile.readline()
    age_list = []
    # Read data until there's no data
    while name != "":
        # Get age
        age = infile.readline()
        # Remove new line
        name = name.rstrip("\n")
        age = age.rstrip("\n")

        age = age
        # Add ages to list
        age_list.append(age)
        name = infile.readline()

    # Display the oldest
    oldest = max(age_list)
    print(f"\nThe oldest person is {oldest} years old.")
    infile.close()


main()
