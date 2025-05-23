from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

my_rec1 = Rectangle(2,8)
my_rec2 = Rectangle(8,8)

print(f"Rectangle1 Length & Width total is : {my_rec1.area()}⚖")
print(f"Rectangle2 Length & Width total is : {my_rec2.area()}⚖")