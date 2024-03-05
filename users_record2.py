users_record = {}

input_line = input()
while input_line != 'done':
    name, email = input_line.split()
    users_record[name] = email
    input_line = input()

sorted_keys = list(sorted(users_record.keys()))
for key in sorted_keys:
    print(f"{key} {users_record.get(key)}")
    
