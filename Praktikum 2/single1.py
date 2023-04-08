#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Mobil:
    def __init__(self, nama_mobil, jenis_mobil):
        self.jenis_mobil = jenis_mobil
        self.nama_mobil = nama_mobil
    
    def bergerak(self):
        print(self.nama_mobil, "bergerak maju")

class Hypercar(Mobil):
    def __init__(self, nama_mobil, jenis_mobil, tipe):
        super().__init__(nama_mobil, jenis_mobil)
        self.tipe = tipe
    
    def bersuara(self):
        print("Bruuuuumum!")

mobilC = Hypercar("Ferrari 488 spider", "Hypercar", "sedan")
mobilC.bergerak() 
mobilC.bersuara() 
