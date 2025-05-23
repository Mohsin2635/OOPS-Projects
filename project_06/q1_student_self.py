class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"student name: {self.name}")
        print(f"student age: {self.age}")
    def Identity(self):
        if self.age > 18:
            print(f"You are eligible to make NIC!💖")
        else:
            print(f"You can't eligible for NIC🙂")
        
student1 = student("Kaleem",19)
student2 = student("hammad",16)
student1.display()
student1.Identity()
student2.display()
student2.Identity()

