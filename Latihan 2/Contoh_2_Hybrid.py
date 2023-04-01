class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

# Single Inheritance
class Mahasiswa(Seseorang):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
    
    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)

# Single Inheritance
class Employee(Seseorang):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary
    
    def get_info(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

# Multiple Inheritance
class Penulis(Employee, Mahasiswa):
    def __init__(self, name, age, address, employee_id, salary, student_id, published_books):
        Employee.__init__(self, name, age, address, employee_id, salary)
        Mahasiswa.__init__(self, name, age, address, student_id)
        self.published_books = published_books
        self.student_id = student_id

    def get_info(self):
        super().get_info()
        print("Student ID:", self.student_id)
        print("Published Books:", self.published_books)
 
mahasiswa = Mahasiswa("Max", 30,"USA","21065778")
mahasiswa.get_info()  
employee = Employee("Rocky", 20, "England","126238282","$500000")
employee.get_info()