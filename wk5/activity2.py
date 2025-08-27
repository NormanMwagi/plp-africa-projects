class Animal: 
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"{self.name} is a {self.species}."

    def move(self):
        # base method (could be abstract in real-world OOP)
        print(f"{self.name} is moving...")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def move(self):
        print(f"{self.name} is running on all fours 🐕")


class Bird(Animal):
    def __init__(self, name, species="Bird"):
        super().__init__(name, species)

    def move(self):
        print(f"{self.name} is flying in the sky 🕊️")


class Fish(Animal):
    def __init__(self, name, species="Fish"):
        super().__init__(name, species)

    def move(self):
        print(f"{self.name} is swimming in the water 🐠")


# --- Demonstration of Polymorphism ---
animals = [
    Dog("Buddy", "Golden Retriever"),
    Bird("Tweety"),
    Fish("Nemo")
]

for animal in animals:
    print(animal)   # calls __str__
    animal.move()   # polymorphism in action
