#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Pelajar:
    def __init__(self, nama, nis):
        self.nama = nama
        self.nis = nis

    def pkl(self):
        print(self.nama, "dengan Nis",self.nis,"sedang PKL di Panasonic")

class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    
    def bekerja(self):
        print(self.nama, "sedang bekerja sebagai", self.pekerjaan, "di pabrik Panasonic")

class PelajarPekerja(Pelajar, Pekerja):
    def __init__(self, nama, nis, pekerjaan):
        Pelajar.__init__(self, nama, nis)
        Pekerja.__init__(self, nama, pekerjaan)

    def jabatan(self):
        print(self.nama,"sedang mendapatkan kenaikan jabatan dari", self.pekerjaan, "menjadi CEO")

mhs_pekerja = PelajarPekerja("Figo", "185432", "Electonical Engineering")
mhs_pekerja.pkl() 
mhs_pekerja.bekerja()  
mhs_pekerja.jabatan() 