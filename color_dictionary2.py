favorite_color = {}

person_name = input()
color_dict = {"red":255, "green":248, "blue":220}
# The dictionary itself is set as the value
favorite_color[person_name] = color_dict

print(f"{person_name}'s favorite color:")
print(f'red: {favorite_color[person_name]["red"]}')
print(f'green: {favorite_color[person_name]["green"]}')
print(f'blue: {favorite_color[person_name]["blue"]}')
