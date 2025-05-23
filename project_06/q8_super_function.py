class Student:
    def __init__(self,name):
        self.name = name
class Teacher(Student):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject = subject

teacher1 = Teacher("Anabiya","English")
teacher2 = Teacher("Ammara","Math")
print(f"The first teacher is miss {teacher1.name}👩".upper())
print(f"Her subject to teaching {teacher1.subject}📚".upper())
print(f"The second teacher is miss {teacher2.name}👩‍🦰".upper())
print(f"The subject to teaching is {teacher2.subject}📕".upper())