class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def find_area(self):
        area = self.length * self.width
        return area

rectangle1 = Rectangle()
print("Rectangle 1")
print("***********")
rectangle1.length = int(input("Enter length: "))
rectangle1.width = int(input("Enter width: "))

rectangle2 = Rectangle()
print("Rectangle 2")
print("***********")
rectangle2.length = int(input("Enter length: "))
rectangle2.width = int(input("Enter width: "))

print(f"First rectangle's area: {rectangle1.find_area()}")
print(f"Second rectangle's area: {rectangle2.find_area()}")
