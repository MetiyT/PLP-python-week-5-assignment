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
