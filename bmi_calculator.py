# A simple bmi calculator

def bmi_calculator():
    print("Welcome to a simple body mass index (bmi) calculator.")
    height = float(input("Please enter your height in inches: "))
    weight = float(input("Please enter your weight in pounds: "))
    bmi = weight / (height * height) * 703

    #print(bmi)

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 25:
        print("You are an optimal weight.")
    elif 25 <= bmi < 30:
        print("You are overweight.")
    elif 30 <= bmi < 35:
        print("You are mildly obese.")
    elif 35 <= bmi < 40:
        print("You are moderately obese.")
    elif bmi >= 40:
        print("You are severely obese.")
    
bmi_calculator()

