#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Mobil:
    def __init__(self, model, warna, tahun):
        self.model = model
        self.warna = warna
        self.tahun = tahun

    def info(self):
        print(f"Model mobil: {self.model}\nWarna mobil: {self.warna}\nTahun pembuatan: {self.tahun}")

    def bahan_bakar(self):
        print("Mobil menggunakan bahan bakar bensin.")

class MobilListrik(Mobil):
    def __init__(self, model, warna, tahun):
        super().__init__(model, warna, tahun)

    def bahan_bakar(self):
        print("Mobil menggunakan baterai sebagai sumber energi.")

mobil1 = Mobil("Sedan", "Hitam", 2022)
mobil2 = MobilListrik("Tesla", "Merah", 2023)

mobil1.info()
mobil1.bahan_bakar()

print("\n")

mobil2.info()
mobil2.bahan_bakar()
