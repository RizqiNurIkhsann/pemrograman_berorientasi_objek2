#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Kendaraan:
    def __init__(self, nama_maskapai, umur_Kendaraan):
        self.nama_maskapai = nama_maskapai
        self.umur_kendaraan = umur_Kendaraan

    def terbang(self):
        print(f"{self.nama_maskapai} dengan pesawat Boeing 737 sedang mengudara di Laut jawa.")

class Pilot(Kendaraan):
    def __init__(self, nama_kendaraan, umur_kendaraan, jenis_kendaraan):
        super().__init__(nama_kendaraan, umur_kendaraan)
        self.jenis_kendaraan = jenis_kendaraan

    def mengudara(self):
        print(f"{self.jenis_kendaraan} dengan nama {self.nama_maskapai} yang berumur {self.umur_kendaraan} Tahun sedang mengudara di Laut jawa")

dosenA = Pilot("Maskapai Citilink Indonesia", 4, "Pesawat")
dosenA.terbang()
dosenA.mengudara() 