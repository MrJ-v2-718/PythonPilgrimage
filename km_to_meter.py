class Length:

    km_to_m = 1000

    def __init__(self):
        self.km = 0
        
    def print_value(self):
        m = self.km * self.km_to_m
        print(f'{self.km} kilometers = {m} meters')

track_length = Length()
track_length.km = int(input("Enter length in km: "))
track_length.print_value()
