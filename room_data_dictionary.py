room_data1 = {'234': 'Taj'}
room_data2 = {}
ref_record1 = room_data1  # For testing purposes, ref_record1 references room_data1
ref_record2 = room_data2  # For testing purposes, ref_record2 references room_data2

input_line = input()
while input_line != 'done':
	room, name = input_line.split()
	room_data2[room] = name
	input_line = input()

room_data1.clear()
room_data1.update(room_data2)

print('Room data 1:')
print(room_data1)
print('Room data 2:')
print(room_data2)
