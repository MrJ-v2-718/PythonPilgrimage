# MrJ
# 1/23/24
# Purpose: Get first name, last name, and salary. Calculate raise.
# Less than 40,000 gets 5% raise
# If over 40,000 gets 2,000 dollars + 2% on everything above 40,000

def main():
    # Variables
    first = ""
    last = ""
    salary = 0.0
    new_salary = 0.0

    # User Input
    first, last, salary = get_data()

    # Create function to determine raise
    new_salary = calc_raise(salary)

    # Create a function to show the results
    show_results(first, new_salary)

def get_data():
    # User Input
    first = input(f"    Enter your first name: ")
    last = input(f"     Enter your last name: ")
    salary = float(input(f"Enter your current salary: "))

    return first, last, salary

def calc_raise(pay):
    if pay <= 40000:
        new_pay = pay * 1.05
    else:
        new_pay = 2000 + ((pay - 40000)*.02) + pay

    return new_pay

def show_results(first, new_salary):
    print(f"{first}, your new salary will be ${new_salary:,.2f}.")

    
main()
