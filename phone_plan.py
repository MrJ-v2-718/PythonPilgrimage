class PhonePlan:

    def __init__(self, num_mins = 0, num_messages= 0):
        self.num_mins = num_mins
        self.num_messages = num_messages

    def print_plan(self):
        print(f'Mins: {self.num_mins}', end=' ')
        print(f'Messages: {self.num_messages}')


my_plan = PhonePlan(int(input("Enter mins: ")), int(input("Enter msgs: ")))
dads_plan = PhonePlan()
moms_plan = PhonePlan(int(input("Enter mins: ")))

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()

print('Mom\'s plan...', end= ' ')
moms_plan.print_plan()
