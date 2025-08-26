#Task 2:
#Function to calculate power:
def power(base, exponent):
    return base ** exponent
#Function to calculate modulo:
def modulo(a, b):
    return a % b
base = 5
exponent = 3
a = 17
b = 4
print(f"{base} raised to the power {exponent} is: {power(base, exponent)}")
print(f"The remainder when {a} is divided by {b} is: {modulo(a, b)}")
