class RectangularPyramid:
    def __init__(self):
        self.base_length = 0
        self.base_width = 0

pyramid1 = RectangularPyramid()
pyramid1.base_length = int(input("Enter base length: "))
pyramid1.base_width = int(input("Enter base width: "))

base_area = pyramid1.base_length * pyramid1.base_width

print(f'Base area: {base_area}')
