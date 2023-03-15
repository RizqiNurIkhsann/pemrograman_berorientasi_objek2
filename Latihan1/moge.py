class Moge: 
    def __init__(self, merk, warna):
        self.warna = warna
        self.merk = merk
    def info(self):
        print(f"Moge {self.merk} berwarna {self.warna}")

mogeA = Moge("Kawasaki", "Hijau")
mogeA.info() 
mogeB = Moge("Ducati", "Hitam Metalic")
mogeB.info()
