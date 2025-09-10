class Animal:
    def move(self):
        print("This animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("Running on four legs 🐕")

class Bird(Animal):
    def move(self):
        print("Flying through the sky 🐦")

class Fish(Animal):
    def move(self):
        print("Swimming in the water 🐠")


zoo = [Dog(), Bird(), Fish()]
for animal in zoo:
    animal.move()
