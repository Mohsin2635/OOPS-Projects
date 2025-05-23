class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __del__(self):
        print(f"Object destroyed for {self.name}")

personName = Person("Hammad",18)