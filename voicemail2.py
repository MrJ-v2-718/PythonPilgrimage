class Voicemail:
    def __init__(self, greeting, number, name): 
        self.greeting = greeting
        self.number = number
        self.name = name

    def update_greeting(self, new_greeting):
        self.greeting = new_greeting

    def print_data(self):
        print(f"Voicemail data: {self.greeting}, {self.number}, {self.name}'s inbox")

greeting1 = input("Enter greeting: ")
number1 = int(input("Enter number: "))
name1 = input("Enter name: ")
new_greeting = input("Enter new greeting: ")

voicemail1 = Voicemail(greeting1, number1, name1)
voicemail1.print_data()
voicemail1.update_greeting(new_greeting)
voicemail1.print_data()

