# While Loop Demo
# Purpose: Get Students Grades, calculate average, find letter grade, print results

# Variables
numGrades = 0
grade = []
firstName = ""
lastName = ""
average = 0.0
totalStudents = 0
more = "y"

# start while loop
while more == "y":
    # Clear list
    grade = []
    # Ask student name
    first_name = input("Enter your first name: ")
    lastName = input("Enter student last name: ")
    print()

    numGrades = int(input("How many grades would you like to enter? "))

    for num in range(numGrades):
        score = int(input("Enter grade: "))
        grade.append(score)

    # Get grade
    average = sum(grade)/numGrades

    # Find letter grade
    if average >= 100:
        letter = "A+"
    elif average > 79 and average <= 89:
        letter = "A"
    elif average > 69 and average <= 79:
        letter = "B"
    elif average > 59 and average <= 69:
        letter = "C"
    elif average < 59:
        letter = "D"
    else:
        letter = "F"

    # Tell if the student passed or failed a class
    if grade == "A+" or "A" or "B" or "C":
        print("You passed")
    else:
        print("You failed")

    # print student info
    print()
    print(f"{firstName} {lastName} has a {average:.2f}% average")
    print(f"Letter grade: {letter}")

    totalStudents += 1

    # sentinel
    more = input("Enter another student? (y/n)")
    print()

# Final statements, number of students entered
if totalStudents == 1:
    print(f"{totalStudents} student grade was calculated.")
else:
    print(f"{totalStudents} student grade was calculated.")





    
    
    
