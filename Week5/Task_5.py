#Task_5: Fully Interactive Polymorphism Example
class Animal:
    def sound(self):
        print("This animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")
class Lion(Animal):
    def sound(self):
        print("Lion says: Roar")
class Tiger(Animal):
    def sound(self):
        print("Tiger says: Grrr")
class Parrot(Animal):
    def sound(self):
        print("Parrot says: Squawk")
class Elephant(Animal):
    def sound(self):
        print("Elephant says: Trumpet")

animal_dict={"1":Animal,"2":Dog,"3":Cat,"4":Lion,"5":Tiger,"6":Parrot,"7":Elephant}

print("Welcome to Interactive Animal Sound Simulator!")
while True:
    print("\nChoose an animal:\n1. Generic Animal\n2. Dog\n3. Cat\n4. Lion\n5. Tiger\n6. Parrot\n7. Elephant\n8. Exit")
    choice=input("Enter choice: ")
    if choice=="8":
        print("Exiting... Goodbye!")
        break
    elif choice in animal_dict:
        obj=animal_dict[choice]()
        obj.sound()
    else:
        print("Invalid choice. Try again.")
