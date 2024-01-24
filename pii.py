# MrJ
# Today
# pii.py
# The purpose of the program is to ask a user the year they were born
# and their name. The program should:
# Call a function that will ask the user for input
# Send that information back to the main function
# Call a function that calculates their age
# Call the funtion to print out their age, first initial, and last name.

# Main function
def main():
    input_list = user_input()
    age_calculator(input_list[2], input_list[3])
    name_printer(input_list[0], input_list[1])


# Function asking the user for input
def user_input():
    input_list = []
    more_info = "y"

    while more_info != "n":
        input_list.append(input(f"   What is your first name? "))
        input_list.append(input(f"    What is your last name? "))
        input_list.append(int(input(f"What year were you born? ")))
        input_list.append(int(input(f"                  What year is it? ")))

        more_info = input("Do you have any more info to enter? (y/n)")
        if more_info == "n":
            return input_list


# Function that calculates the age
def age_calculator(birth_year, current_year):
    age = current_year - birth_year
    age_printer(age)
    return age


# Function that prints the age
def age_printer(age):
    print(f"{age} ", end="")


# Function that prints first initial and last name
def name_printer(first_name, last_name):
    first_initial = first_name[0]
    print(f"{first_initial}. {last_name}")


main()
