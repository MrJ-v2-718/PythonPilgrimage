temperature = 76

if 'New York' in temperature:
    if temperature['New York'] > 90:
        print('The city is melting!')
    else:
        print(f"The temperature in New York is {temperature['New York']}.")
else:
    print('The temperature in New York is unknown.')
