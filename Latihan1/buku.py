class Buku:
    def __init__(self, judul, penulis, tahunterbit):
        self.judul = judul
        self.penulis = penulis
        self.tahunterbit = tahunterbit
    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}\nTahun Terbit: {self.tahunterbit}")
bukuA = Buku("Belajar Menjadi Programer", "Muhammad Rizqi Nur Ikhsannudin", "terbit tahun 2020")
bukuA.info()