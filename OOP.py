# Parent class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery   # private (encapsulation)

    # Encapsulation: getter for battery
    def get_battery(self):
        return f"{self.__battery}% battery remaining"

    # Method to charge battery
    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Charged! Now at {self.__battery}% 🔋"

    # Default action (polymorphism target)
    def action(self):
        return f"{self.model} is making a call 📞"


# Child class (Inheritance + Polymorphism)
class SmartphonePro(Smartphone):
    def __init__(self, brand, model, battery, stylus=True):
        super().__init__(brand, model, battery)
        self.stylus = stylus

    def use_stylus(self):
        return "Using stylus 🖊️" if self.stylus else "No stylus available!"

    # Override action()
    def action(self):
        return f"{self.model} is taking a high-res photo 📸"


# Another Child class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling=True):
        super().__init__(brand, model, battery)
        self.cooling = cooling

    # Override action()
    def action(self):
        return f"{self.model} is playing a game 🎮"


# Demonstration
phone1 = Smartphone("Samsung", "Galaxy S22", 80)
phone2 = SmartphonePro("Apple", "iPhone 15 Pro", 50)
phone3 = GamingPhone("Infinix", "Hot 50 pro", 60)

# Store them in a list for polymorphism
phones = [phone1, phone2, phone3]

# Show polymorphic behavior
for p in phones:
    print(p.action()) 

print(phone1.get_battery())
print(phone2.use_stylus())
print(phone3.charge(30))
