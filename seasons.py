# A program that takes a month as input and outputs the current season.
input_month = input().lower()
input_day = int(input())
if input_day 

# Checks
valid_months = ["january", "february", "march", "april", "may", "june", "july",
                "august", "september", "october", "november", "december"]

cusp_months = ["march", "june", "september", "december"]

if input_month in valid_months:
    if input_month in cusp_months:
        if (input_month == "march") & (19 < input_day < 32):
            print("Spring")
        elif (input_month == "march") & (0 < input_day < 20):
            print("Winter")
        elif (input_month == "june") & (0 < input_day < 21):
            print("Spring")
        elif (input_month == "june") & (20 < input_day < 31):
            print("Summer")
        elif (input_month == "september") & (0 < input_day < 22):
            print("Summer")
        elif (input_month == "september") & (21 < input_day < 31):
            print("Autumn")
        elif (input_month == "december") & (0 < input_day < 22):
            print("Summer")
        elif (input_month == "december") & (20 < input_day < 32):
            print("Summer")
        else:
            print("Invalid")
    elif (input_month == "january") & (0 < input_day < 32):
        print("Winter")
    elif (input_month == "february") & (0 < input_day < 29):
        print("Winter")
    elif (input_month == "april") & (0 < input_day < 31):
        print("Spring")
    elif (input_month == "may") & (0 < input_day < 32):
        print("Spring")
    elif (input_month == "july") & (0 < input_day < 32):
        print("Summer")
    elif (input_month == "august") & (0 < input_day < 32):
        print("Summer")
    elif (input_month == "october") & (0 < input_day < 32):
        print("Autumn")
    elif (input_month == "november") & (0 < input_day < 31):
        print("Autumn")
    else:
        print("Invalid")
else:
    print("Invalid")
