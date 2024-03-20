class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

#   def ... Add new method here ...
    def calculate_pay(self):
        pay = self.wage * self.hours_worked
        return pay

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print(f'Alice:\n Net pay: {alice.calculate_pay():.2f}')

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print(f'Barbara:\n Net pay: {barbara.calculate_pay():.2f}')

