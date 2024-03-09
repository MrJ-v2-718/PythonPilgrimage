# MrJ
# 1/16/24
# Purpose: While demo, calc average grade

# Variables
grade = 0.0
average = 0.0
total = 0.0

enter_grades = "y"
loops = 0

while enter_grades == "y":
    grade = float(input("Grade: "))
    total += grade
    loops += 1
    enter_grades = input("More grades?(y/n)")

average = total / loops
print(f"Average is {average:.2f}")
