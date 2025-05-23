class A:
    def show(self):
        print("I'm from class A")
class B(A):
    def show(self):
        print("I'm from class B")
class C(A):
    def show(self):
        print("I'm from class C")
class D(B,C):  #ye D class 2 yaani multiple inherotence krry hai isko kehty hain diamond inheritence
        pass

d = D()
d.show()

# print(D.__mro__)