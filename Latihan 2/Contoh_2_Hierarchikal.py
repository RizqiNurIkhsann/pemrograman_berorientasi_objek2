class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
    
    def get_department(self):
        return self.department


class Programmer(Employee):
    def __init__(self, name, age, salary, language):
        super().__init__(name, age, salary)
        self.language = language
    
    def get_language(self):
        return self.language


class SeniorProgrammer(Programmer):
    def __init__(self, name, age, salary, language, level):
        super().__init__(name, age, salary, language)
        self.level = level
    
    def get_level(self):
        return self.level
    
manager = Manager("Edith", 30, 40000, "Moonton")
print("Name:", manager.get_name())
print("Age:", manager.get_age())
print("Salary:", manager.get_salary())
print("Department:", manager.get_department())
print("=============================")
programmer = Programmer("Pharsa", 25, 20000, "Python")
print("Name:", programmer.get_name())
print("Age:", programmer.get_age())
print("Salary:", programmer.get_salary())
print("Language:", programmer.get_language())
print("=============================")
sp = SeniorProgrammer("Khufra", 31, 34000, "Python", "Master")
print("Name:", sp.get_name())
print("Age:", sp.get_age())
print("Salary:", sp.get_salary())
print("Language:", sp.get_language())
print("Level:", sp.get_level())
