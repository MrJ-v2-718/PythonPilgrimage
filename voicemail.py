class Voicemail:
    def __init__(self, number, greeting, name):

        self.number = number
        self.greeting = greeting
        self.name = name

number2 = int(input("Enter phone number: "))
greeting2 = input("Enter greeting: ")
name2 = input("Enter name: ")

voicemail1 = Voicemail(768456, 'Please leave a message for Rob', 'Rob')
voicemail2 = Voicemail(number2, greeting2, name2)

print(f"voicemail1 data: {voicemail1.number}, {voicemail1.greeting}, {voicemail1.name}'s inbox")
print(f"voicemail2 data: {voicemail2.number}, {voicemail2.greeting}, {voicemail2.name}'s inbox")
