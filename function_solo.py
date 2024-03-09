# Function Review
# Purpose: Get user name, print initials. Use 4 functions: main(), get info, index, print

def main():
    # variables
    make = ""
    model = ""
    car_year = 0
    miles = 0
    current_year = 0
    vehicle_age = 0

    again = "y"

    while again == "y":
        # call functions
        make, model, car_year, miles, current_year = getUserData()
        vehicle_age = calcAge(current_year, car_year)
        printResults(vehicle_age, if_over)

        # add running total
        count+=1

        # prevent infinite loop
        again = input("Would you like to enter more info? (yes/no) ")
        print()
        
    print()

    
    # Calculation for determining if the vehicle is over 100,000 miles or not
    if miles > 100000:
        if_over = "is over"
    else:
        if_over = "is not over"

def getUserData():
    # input statements
    make = input("Enter make of vehicle: ")
    model = input("Enter model of vehicle: ")
    car_year = int(input("Enter year of vehicle: "))
    miles = int(input("Enter miles of vehicle: "))
    current_year = int(input("Enter current year: "))

    return make, model, car_year, miles, current_year

def calcAge(current_year, car_year):
    # Calculation for determining how old the car is given the year of the vehicle
    vehicle_age = current_year - car_year

    return vehicle_age




def printResults(vehicle_age, if_over):
    print()
    print(f"Your car is {vehicle_age} years old and {if_over} 100,000 miles.")

main()

