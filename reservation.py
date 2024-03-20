class Reservation:
    def __init__(self, num_in_party, preordered, name):
        self.num_in_party = num_in_party
        self.preordered = preordered
        self.name = name

num_in_party1 = int(input())
preordered1 = input()
name1 = input()
num_in_party2 = int(input())
preordered2 = input()
name2 = input()

reservation1 = Reservation(num_in_party1, preordered1, name1)
reservation2 = Reservation(num_in_party2, preordered2, name2)

print(f'reservation1 data: {reservation1.num_in_party} guests, Food preordered: {reservation1.preordered}, {reservation1.name}')
print(f'reservation2 data: {reservation2.num_in_party} guests, Food preordered: {reservation2.preordered}, {reservation2.name}')
