# Color Dictionary
color_dict = {"red":248, "green": 248, "blue": 255}
key_read = input("Enter a color to add: ")
value_read = input("Enter a value: ")
color_dict[key_read] = value_read

print(f'red: {color_dict["red"]}')
print(f'green: {color_dict["green"]}')
print(f'blue: {color_dict["blue"]}')
print(f'{key_read}: {color_dict[key_read]}')

