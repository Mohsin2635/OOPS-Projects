class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
         print(f"{self.name} is a {self.breed} and is very hungry 😋")

dog = Dog("Oloo", "German Shepherd")
dog.bark()