# A program that calculates a dystopian form of sales tax based on age.
subtotal = float(input("Enter the subtotal: "))
age = float(input("Enter your age: "))

age_tax = (age * 0.01) * subtotal
total = age_tax + subtotal

print(f"  Subtotal: ${subtotal:.2f}")
print(f"Living Tax: ${age_tax:.2f}")
print(f"     Total: ${total:.2f}")
