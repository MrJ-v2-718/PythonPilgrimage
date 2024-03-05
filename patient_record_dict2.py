patients_info = {'Rob': 75, 'Fay': 10}

print('Original patients info:')
print(patients_info)

string_input = ""
while string_input != "exit":
    string_input = input()
    if string_input in patients_info:
        del patients_info[string_input]

print('Updated patients info:')
print(patients_info)
