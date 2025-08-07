import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius
circle1 = Circle(5)
area = circle1.cal
perimeter = circle1.calculate_perimeter()
print(f"The perimeter of the circle is: {perimeter:.2f}")