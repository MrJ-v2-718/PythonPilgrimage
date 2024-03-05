"""
Integer num_data is read from input, 
representing the number of remaining strings 
in the input. Use a for loop to read the remaining 
strings from input. Each string consists of a key 
string and a value integer separated by a space. 
Add each key-value pair into the dictionary 
patients_record.
"""

patients_record = {}
num_data = int(input())

for data in range(num_data):
    key_string, value_string = input().strip().split()
    patients_record[key_string] = int(value_string)

print('Patients record:')
print(patients_record)
