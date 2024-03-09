#Dealing with user inputs

name = input("What is your name? ")
print("Hello " + name)

birth_year = input("Enter your birth year: ")
current_year = input("What year is it currently? ")
# the years received as input from the user are stored as strings

# in order to perform calculations with them, we need to convert them to integers
age = int(current_year) - int(birth_year)
# we then, cast them back into a string for output
age = str(age)
print("You are " + age + " years old.")
# the method of "casting" can be used for float and bool as well
