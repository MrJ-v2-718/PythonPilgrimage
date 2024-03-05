users_record = {}

input_line = input()
while input_line != 'exit':
    name, email = input_line.split()
    users_record[name] = email
    input_line = input()

sorted_values = list(sorted(users_record.values()))

print(sorted_values)
