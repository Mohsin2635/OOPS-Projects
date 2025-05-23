class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display_info(self):
         print(f"Employee Name: {self.name}")
         print(f"Employee Age: {self.age}")
         print(f"Employee Salary: {self.salary} 💸")

class Department:
    def __init__(self,department_name,employee):
        self.department_name = department_name
        self.employee = employee    #aggregation hui yaha pr vs composition hy jo
    def display_department_info(self):
        print(f"\nDepartment Name: {self.department_name} 🏢")
        print("Employee Details:")
        self.employee.display_info()

employee_1 = Employee("hammad",19,700000)
hr_department = Department("Human resources", employee_1)
hr_department.display_department_info()

employee_2 = Employee("Saad",24,900000)
markiting_department = Department("Markinting",employee_2)
markiting_department.display_department_info()

