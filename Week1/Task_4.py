#Task 4:
import math
def area_trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height
def area_ellipse(a, b):
    return math.pi * a * b
b1 = float(input("Enter the length of base 1 of trapezoid: "))
b2 = float(input("Enter the length of base 2 of trapezoid: "))
h = float(input("Enter the height of trapezoid: "))
a = float(input("\nEnter the semi-major axis of the ellipse: "))
b = float(input("Enter the semi-minor axis of the ellipse: "))
trapezoid_area = area_trapezoid(b1, b2, h)
ellipse_area = area_ellipse(a, b)
print(f"\nArea of Trapezoid: {trapezoid_area:.2f}")
print(f"Area of Ellipse: {ellipse_area:.2f}")