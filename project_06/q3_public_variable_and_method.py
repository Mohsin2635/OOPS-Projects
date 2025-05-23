class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print(f"Car is starting : Brand {self.brand}")
car1 = Car("Honda")
print(car1.brand)
car1.start()