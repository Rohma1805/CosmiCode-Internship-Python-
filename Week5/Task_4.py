#Task_4:
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return ComplexNumber(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return ComplexNumber(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        r = self.real*other.real - self.imag*other.imag
        i = self.real*other.imag + self.imag*other.real
        return ComplexNumber(r,i)
    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        r = (self.real*other.real + self.imag*other.imag)/denom
        i = (self.imag*other.real - self.real*other.imag)/denom
        return ComplexNumber(r,i)
    def __str__(self):
        return f"{self.real} + {self.imag}i" if self.imag>=0 else f"{self.real} - {abs(self.imag)}i"

#--------------- User Input ----------------
r1 = float(input("Enter real part of first complex number: "))
i1 = float(input("Enter imaginary part of first complex number: "))
r2 = float(input("Enter real part of second complex number: "))
i2 = float(input("Enter imaginary part of second complex number: "))

c1 = ComplexNumber(r1,i1)
c2 = ComplexNumber(r2,i2)

print("\nc1 =",c1)
print("c2 =",c2)

op = input("Choose operation (+, -, *, /): ")
if op=='+':
    print("Result:",c1+c2)
elif op=='-':
    print("Result:",c1-c2)
elif op=='*':
    print("Result:",c1*c2)
elif op=='/':
    if c2.real==0 and c2.imag==0:
        print("Division by zero not allowed")
    else:
        print("Result:",c1/c2)
else:
    print("Invalid operation")