#Week6_Task2: Exception Handling in Complex Math Calculations
import math

def formula1(a,b):
    return (math.sqrt(a)/b)+(a**b)   # sqrt + power

def formula2(a,b):
    return math.log(a)/b             # log division

def formula3(a,b):
    return math.sin(a)+math.cos(b)   # trigonometric

def formula4(a,b):
    return (a/b)+(b/a)               # reciprocal division

def calculate(choice,a,b):
    try:
        if choice=="1":
            result=formula1(a,b)
        elif choice=="2":
            result=formula2(a,b)
        elif choice=="3":
            result=formula3(a,b)
        elif choice=="4":
            result=formula4(a,b)
        else:
            print("Invalid formula choice")
            return
        print("Result:",result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input (negative sqrt or log of non-positive).")
    except OverflowError:
        print("Error: Calculation result is too large.")
    except Exception as e:
        print("Unexpected error:",e)

while True:
    print("\nComplex Calculation Menu")
    print("1. (√a / b) + a^b")
    print("2. log(a) / b")
    print("3. sin(a) + cos(b)")
    print("4. (a/b) + (b/a)")
    print("5. Exit")
    ch=input("Choose formula: ")
    if ch=="5":
        break
    try:
        a=float(input("Enter value of a: "))
        b=float(input("Enter value of b: "))
        calculate(ch,a,b)
    except ValueError:
        print("Error: Please enter numeric values only.")