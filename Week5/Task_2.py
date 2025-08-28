#Task_2:
import math
#Base class
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
#Derived class:Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
#Derived class:Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
#Derived class:Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c
#---------------- Testing ----------------
#Circle
circle = Circle(5)
print(f"Circle: Area = {circle.area():.2f}, Perimeter = {circle.perimeter():.2f}")
#Rectangle
rectangle = Rectangle(4, 6)
print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")
#Triangle
triangle = Triangle(3, 4, 5)
print(f"Triangle: Area = {triangle.area():.2f}, Perimeter = {triangle.perimeter()}")