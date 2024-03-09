# MrJ
# 11/27/2023
# chicago_bulls.py
# Purpose: Develop a program for the 1997 Chicago Bulls that will record
# their player's total points over the season.

# Main Function - Controls the Program
def main():
    # Initialization
    choice = 0

    while choice <= 4:
        # display menu
        menu()
        choice = int(input("\nEnter your menu choice: "))

        if choice == 1:
            add_person()
        elif choice == 2:
            display_data()
        elif choice == 3:
            display_average()
        elif choice == 4:
            display_highest()
        else:
            print("Goodbye.")


# Show Menu Function - Displays Menu
def menu():
    print("MENU")
    print("1 - Add player's data to file")
    print("2 - Display players and their total points")
    print("3 - Calculate the Average")
    print("4 - Display the highest total points")
    print("5 - Exit")


# Saves Entered Player Information Into File Function
def add_person():
    outfile = open("points.txt", "a")
    name = input("Enter name: ")
    points = input("Enter points: ")

    # Write name and age to file
    outfile.write(f"{name}\n")
    outfile.write(f"{points}\n")

    # Close the file
    outfile.close()
    print("Data added to the file.")


# Display the Data Function - Pulls Data From the File
def display_data():
    # Variables
    name = ""
    points = ""

    # Open the file
    infile = open("points.txt", "r")

    # Reading the first name
    name = infile.readline()
    print(f"\nNAME                  POINTS")

    # While loop to read until there's no data
    while name != "":
        # Get points
        points = infile.readline()
        # Remove new line
        name = name.rstrip("\n")
        points = points.rstrip("\n")

        # Print name and points
        print(f"{name:15}       {points}")

        name = infile.readline()
    infile.close()


# Calculate and Display the Average Function
def display_average():
    infile = open("points.txt", "r")
    # Read first name
    name = infile.readline()
    point_list = []
    # Read data until there's no data
    while name != "":
        # Get points
        points = infile.readline()
        # Remove new line
        name = name.rstrip("\n")
        points = points.rstrip("\n")

        points = int(points)
        # Add points to list
        point_list.append(points)
        name = infile.readline()

    # Display the average
    average = sum(point_list) / len(point_list)
    print(f"\nThe average is {average}.")
    infile.close()


# Calculate and Display the Highest Score Function
def display_highest():
    infile = open("points.txt", "r")
    # Read first name
    name = infile.readline()
    point_list = []
    # Read data until there's no data
    while name != "":
        # Get points
        points = infile.readline()
        # Remove new line
        name = name.rstrip("\n")
        points = points.rstrip("\n")

        points = int(points)
        # Add points to list
        point_list.append(points)
        name = infile.readline()

    # Display the highest
    highest = max(point_list)
    print(f"\nThe highest score is {highest} points.")
    infile.close()


main()
