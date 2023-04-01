class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

class Mammal(Animal):
    def __init__(self, name, color, fur):
        super().__init__(name, color)
        self.fur = fur
        
    def get_fur(self):
        return self.fur
    
class Bird(Animal):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan
       
    def get_wingspan(self):
        return self.wingspan
        
# Hierarchical Inheritance
class Reptile(Mammal):
    def __init__(self, name, color, fur, scale):
        super().__init__(name, color, fur)
        self.scale = scale

    def get_scale(self):
        return self.scale
    
# Sample Usage
m = Mammal("Kucing", "Putih-Hitam", "Persia")
print("Nama hewan:",m.get_name()) 
print("Warna:", m.get_color()) 
print("Jenis bulu:", m.get_fur())
print("=============================")
b = Bird("Gagak", "Hitam","panjang")
print("Nama hewan:",b.get_name()) 
print("Warna:",b.get_color()) 
print("Lebar sayap:", b.get_wingspan())
print("=============================")
r = Reptile("Kadal", "Abu-abu", "Halus","Sisik Halus")
print("Nama hewan:",r.get_name()) 
print("Warna:",r.get_color()) 
print("Jenis bulu:", r.get_fur()) 
print("Jenis sisik:",r.get_scale())