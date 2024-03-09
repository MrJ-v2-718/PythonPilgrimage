# MrJ
# for Alive

# Variables
years_alive = int(input("How many years have you existed? "))
MINUTES_IN_YEAR = 525600
minutes_alive = 0

# Processing
for x in range(years_alive):
    minutes_alive += 525600

print(f"You have lived for {minutes_alive} minutes!")
