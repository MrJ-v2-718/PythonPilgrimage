class Length:
    show_in_cm = True
      
    def __init__(self):
        self.value_in_m = 0
  
    def print_value(self):

        if self.show_in_cm == True:
            print(f"Length in centimeters: {self.value_in_m * 100}")
        else:
            print(f"Length in meters: {self.value_in_m}")
  
cord_length1 = Length()
cord_length1.value_in_m = int(input("Enter amount in meters: "))
print(f'First length measurement: {cord_length1.value_in_m}')
cord_length1.print_value()

Length.show_in_cm = False

cord_length2 = Length()
cord_length2.value_in_m = int(input("Enter amount in meters: "))
print(f'Second length measurement: {cord_length2.value_in_m}')
cord_length2.print_value()
