#Task1: 
import time
def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} executed in {end-start:.6f} sec")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Slow function finished")

@timer
def add_numbers(a,b):
    print("Sum:",a+b)

while True:
    print("\nChoose function:\n1. Slow Function\n2. Add Numbers\n3. Exit")
    ch=input("Enter choice: ")
    if ch=="1": slow_function()
    elif ch=="2":
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        add_numbers(a,b)
    elif ch=="3": break
    else: print("Invalid choice, try again.")