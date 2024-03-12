# MrJ
# 3/11/2024
# Purpose: Create a dictionary of names and birth dates.
# Each entry in the dictionary uses a name as the key and the 
# birthday as the value.
# The program will display a menu that allows the user to:
# -Show the names and birthdays in the dictionary
# -Look up a birthday by using the name of the person
# -Add a new person and their birthday
# -Change a birthday
# -Delete a person and their birthday
# -Save the dictionary to a file
# -Show how old the person is this year
# -Quit the program
# I have not copied this code from anyone or from any website.

def main():
	birthday_loop()


def birthday_loop():
	# Variables
	birthdays = {}
	program_running = "y"
	
	#Main Program Loop
	while program_running == "y":
		display_menu()
		choice = input("Enter a menu choice: ").strip()
		if choice == "1":
			# 1. Show the names and birthdays in the dictionary
			#print(birthdays)
			for name, birthday in birthdays.items():
				print(name + " " + birthday)
		elif choice == "2":
			# 2. Look up a birthday by using the name of the person
		    name = input("Enter a name to lookup: ")
		    if name in birthdays:
		    	print(f"{name}'s birthday is on {birthdays[name]}.")
		    else:
		    	print("Entry does not exist.")
		    	continue
		elif choice == "3":
			# 3. Add a new person and their birthday
		    name = input("Enter a name: ").strip().title()
		    birthday = input("Enter a birthday (mm/dd/yyyy): ").strip()
		    birthdays[name] = birthday
		elif choice == "4":
			# 4. Change a birthday
		    name = input("Enter a name to change: ").strip().title()
		    if name in birthdays:
		    	birthdays[name] = input("Enter new birthday: ")
		    else:
		    	print("Entry does not exist.")
		elif choice == "5":
			# 5. Delete a person and their birthday
		    name = input("Enter a name to delete: ").strip().title()
		    if name in birthdays:
		    	del birthdays[name]
		    else:
		    	print("Entry does not exist.")
		    	continue
		elif choice == "6":
			# 6. Save the dictionary to a file
		    filename = "birthdays.txt"
		    with open(filename, "w") as f:
		    	for name, birthday in birthdays.items():
		    		f.write(f"{name} {birthday}\n")
		elif choice == "7":
			# 7. See how old the person is this year
		    name = input("Enter a name to lookup: ").strip().title()
		    if name in birthdays:
		    	current_year = input("What year is it: ").strip()
		    	birth_month, birth_day, birth_year = birthdays[name].split("/")
		    	try:
		    		age = int(current_year) - int(birth_year)
		    		print(f"{name} turns {age} this year.")
		    	except ValueError:
		    		print("That is not a valid year.")
		    		continue
		    else:
		    	print("Entry does not exist.")
		    	continue
		elif choice == "8":
			# 8. Quit the program
		    program_running = "n"
		else:
		    print('Not a valid choice.')
		    continue


def display_menu():
	print()
	print(f"            Birthday Dictionary")
	print("*************************************************")
	print("1. Show the names and birthdays in the dictionary\n"
		  "2. Look up a birthday by using the name of the person\n"
		  "3. Add a new person and their birthday\n"
		  "4. Change a birthday\n"
		  "5. Delete a person and their birthday\n"
		  "6. Save the dictionary to a file\n"
		  "7. See how old the person is this year\n"
		  "8. Quit the program\n")
		  
main()

