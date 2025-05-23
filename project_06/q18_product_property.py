class Product:
    def __init__(self,price):
        self._price = price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value < 0 :
            print("Negative Value is not allowed!")
        else:
            self._price = value
    
    @price.deleter
    def price(self):
        print("Price will be deleting...")
        del self._price
    
p = Product(500)
p.price = 200
print(p.price)

p.price = -100
del p.price

        