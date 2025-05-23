def add_greeting(cls):
    def greet(self):
        print("Hello from Decorator!👋")
    cls.greet = greet
    return cls   
@add_greeting
class Person:
    pass

p = Person()
p.greet()