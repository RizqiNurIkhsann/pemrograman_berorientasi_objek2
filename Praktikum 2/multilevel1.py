#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary
    
    def get_details(self):
        super().get_details()
        print(f"ID: {self.id}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, age, id, salary, department):
        super().__init__(name, age, id, salary)
        self.department = department
    
    def get_details(self):
        super().get_details()
        print(f"Department: {self.department}")

person = Person ("Agus",30)
person.get_details()
employee = Employee("Asep",25,"21323243","$20000")
employee.get_details()
manager = Manager ("Budi", 23, "11263628", "$30000", "Keuangan")
manager.get_details()