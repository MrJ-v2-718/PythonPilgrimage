temperatures = 76

if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print('The city is melting!')
    else:
        print(f"The temperature in New York is {temperatures['New York']}.")
else:
    print('The temperature in New York is unknown.')
