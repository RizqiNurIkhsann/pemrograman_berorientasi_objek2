#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Person:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} speaks")

class Human(Person):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
    
    def eat(self):
        print(f"{self.name} eats too much and becomes fat {self.weight} kg")

class fadli(Human):
    def __init__(self, name, weight, skin_color):
        super().__init__(name, weight)
        self.skin_color = skin_color
    
    def color_skin(self):
        print(f"{self.name} has {self.skin_color} skin color ")

parrot = fadli("Fadli", 80, "brown")
parrot.speak()
parrot.eat() 
parrot.color_skin() 