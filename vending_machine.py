class VendingMachine:
    def __init__(self):
        self.money_inserted = 0

    def dispense(self):
        self.money_inserted += 0.75

gumball_dispenser1 = VendingMachine()
for i in range(int(input("Enter # of gumballs @ 75 cents: "))):
    gumball_dispenser1.dispense()
print(f'The first gumball dispenser collected ${gumball_dispenser1.money_inserted:.2f}.')

gumball_dispenser2 = VendingMachine()
for i in range(int(input("Enter # of gumballs @ 75 cents: "))):
    gumball_dispenser2.dispense()
print(f'The second gumball dispenser collected ${gumball_dispenser2.money_inserted:.2f}.')
