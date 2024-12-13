from abc import ABC

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
class Employee(User):
    def __init__(self,name,email,phone,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age=age
        self.designation=designation
        self.salary=salary
class Admin(User):
    def __init__(self,name,phone,email,address):
        self.employees=[]
        
    def add_employee(self,name,email,phone,address,age,designation,salary):
       employee=Employee(name,email,phone,address,age,designation,salary)
       self.employees.append(employee)
       print(f'{name} is added')
        
    def view_employee(self):
        print("Employee List!!")
        for emp in self.employees:
            print(emp.name,emp.email,emp.phone,emp.address)
ad=Admin("Karim",'017752828228','heioya@gmail.com','barishal')
ad.add_employee('Shagro','email@gmail.com','01785228888','Khulna','32','Chef','200000')
ad.view_employee()