#Task_3
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def display_info(self):
        print(f"Brand: {self.brand}, Max Speed: {self.max_speed} km/h")
class Car(Vehicle):
    def __init__(self, brand, max_speed, doors):
        super().__init__(brand, max_speed)
        self.doors = doors
    def display_info(self):
        print(f"Car Brand: {self.brand}, Max Speed: {self.max_speed} km/h, Doors: {self.doors}")
class Bike(Vehicle):
    def __init__(self, brand, max_speed, type_bike):
        super().__init__(brand, max_speed)
        self.type_bike = type_bike
    def display_info(self):
        print(f"Bike Brand: {self.brand}, Max Speed: {self.max_speed} km/h, Type: {self.type_bike}")
car1 = Car("Toyota", 180, 4)
bike1 = Bike("Yamaha", 120, "Sport")
car1.display_info()
bike1.display_info()
