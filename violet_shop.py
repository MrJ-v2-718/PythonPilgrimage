class Violet:
    def __init__(self):
        self.price = 0

    def find_total_cost(self, violet_count):
        total_cost = violet_count * self.price
        return total_cost

small_order = Violet()
small_order.price = float(input("Enter small order price: "))

large_order = Violet()
large_order.price = float(input("Enter large order price: "))

print(f'Total cost of small violet purchase: {small_order.find_total_cost(int(input("Enter small order amount: "))):.2f}')
print(f'Total cost of large violet purchase: {large_order.find_total_cost(int(input("Enter large order amount: "))):.2f}')
