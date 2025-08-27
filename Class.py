class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number} 📞")

    def charge(self, amount):
        self.battery += amount
        print(f"{self.brand} {self.model} charged to {self.battery} mAh 🔋")

# Derived class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        print(f"Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system 🎮")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S23", 128, 4000)
phone2 = GamingPhone("Asus", "ROG Phone 6", 256, 6000, "Advanced Liquid Cooling")

phone1.call("123-456-7890")
phone2.play_game("Call of Duty")
phone2.charge(500)


class Vehicle:
    def move(self):
        pass  # Base class does nothing

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛴️")

# Testing polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

