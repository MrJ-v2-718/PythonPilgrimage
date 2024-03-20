class StudentDetails:
    def __init__(self):
        self.birthplace = 'unknown'
        self.credit_hr = 0

new_student = StudentDetails()
new_student.birthplace = input("Enter birthplace: ")
new_student.credit_hr = int(input("Enter credit hours: "))

print(f"Birthplace: {new_student.birthplace}")
print(f"Credits: {new_student.credit_hr}")
