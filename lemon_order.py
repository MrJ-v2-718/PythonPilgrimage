class LemonOrder:
    orders_count = 0
    
    def __init__(self):
        self.num_lemons = 0

    def cook(self, lemons_used):

        LemonOrder.orders_count += 1
        self.num_lemons = lemons_used
        print(f"One order made for {self.num_lemons} lemons")
    
total_lemons_ordered = 0
for token in input("How many lemons would you like? ").split():
    lemon_order = LemonOrder()
    lemon_order.cook(int(token))
    total_lemons_ordered += lemon_order.num_lemons
print(f'Number of lemon orders: {LemonOrder.orders_count}')
print(f'Total number of lemons ordered: {total_lemons_ordered}')
