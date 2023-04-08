#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pekerja:
    def __init__(self, pekerjaan, gaji):
        self.pekerjaan = pekerjaan
        self.gaji = gaji

    def display_info(self):
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")

class Pilot:
    def __init__(self, maskapai, pangkat):
        self.maskapai = maskapai
        self.pangkat = pangkat

    def display_info(self):
        print(f"Maskapai: {self.maskapai}")
        print(f"Pangkat: {self.pangkat}")

class PilotPekerja(Manusia, Pekerja, Pilot):
    def __init__(self, nama, umur, pekerjaan, gaji, maskapai, pangkat):
        Manusia.__init__(self, nama, umur)
        Pekerja.__init__(self, pekerjaan, gaji)
        Pilot.__init__(self, maskapai, pangkat)

    def display_info(self):
        super().display_info()
        print(f"Pekerjaan: {self.pekerjaan}")
        print(f"Gaji: {self.gaji}")
        print(f"Maskapai: {self.maskapai}")
        print(f"Pangkat: {self.pangkat}")

# contoh penggunaan
penulis_pekerjaC = PilotPekerja("Vincent Raditya", 25, "Pilot", "$5343", "Garuda Indonesia", "Captain")
penulis_pekerjaC.display_info()