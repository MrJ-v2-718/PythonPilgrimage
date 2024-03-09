# for Loop Demo

# Variables
num = 0.0
total = 0.0
average = 0.0
num_grades = 0

# Get Number of Grades to Enter
num_grades = int(input("How many grades do you need to enter? "))

# Processing
for grade in range(num_grades):
    num = float(input("Grade: "))
    total += num

average = total / num_grades

print(f"Average: {average}%")
