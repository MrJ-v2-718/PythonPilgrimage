doctors_room = {'Pham': 349, 'Rice': 399, 'Ruiz': 325, 'Shah': 595}
patient_directory = {325: 'Pat', 349: 'Dan', 399: 'Tia', 595: 'Ron'}

doctor_name = input()

room_num = doctors_room.get(doctor_name, -99)
patient_name = patient_directory.pop(room_num, "nobody")

print(f'{doctor_name} (room {room_num}) is seeing {patient_name}.')
print('Remaining patients:')
print(patient_directory)
