contact_list = {}

input_line = input().split("\n")
input_query = input()

for line in input_line:
    name_number = line.split()
    for name in name_number:
        name, number = name.split(",")
        contact_list[name] = number
#print(contact_list)
print(contact_list.get(input_query, "N/A"))

