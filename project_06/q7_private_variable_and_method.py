class Employee:
    def __init__(self,name,_salary,__pvt):
        self.name = name
        self._salary = _salary
        self.__pvt = __pvt
Final_Data = Employee("Anas",120000,"123-456-789")

print(Final_Data.name)
print(Final_Data._salary)
print(Final_Data._Employee__pvt)