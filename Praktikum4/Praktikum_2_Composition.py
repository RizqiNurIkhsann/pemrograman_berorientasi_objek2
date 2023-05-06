class KelompokKKM:
    def __init__(self, nama, jumlah_anggota):
        self.nama = nama
        self.jumlah_anggota = jumlah_anggota
        self.mahasiswas = []

    def tambah_mahasiswa(self, mahasiswa):
        if len(self.mahasiswas) < self.jumlah_anggota:
            self.mahasiswas.append(mahasiswa)
            mahasiswa.kelompok = self
        else:
            print("Jumlah anggota kelompok sudah maksimal")

    def daftar_mahasiswa(self):
        print(f"Daftar Mahasiswa Kelompok {self.nama}:")
        for mahasiswa in self.mahasiswas:
            print(f"- {mahasiswa.nama}")

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.kelompok = None

    def bergabung_kelompok(self, kelompok):
        kelompok.tambah_mahasiswa(self)

    def keluar_kelompok(self):
        if self.kelompok:
            self.kelompok.mahasiswas.remove(self)
            self.kelompok = None

# Contoh penggunaan
kelompok1 = KelompokKKM("Kelompok 1", 4)

mahasiswa1 = Mahasiswa("Andi", "19001")
mahasiswa2 = Mahasiswa("Budi", "19002")
mahasiswa3 = Mahasiswa("Cindy", "19003")
mahasiswa4 = Mahasiswa("Dewi", "19004")
mahasiswa5 = Mahasiswa("Eka", "19005")

mahasiswa1.bergabung_kelompok(kelompok1)
mahasiswa2.bergabung_kelompok(kelompok1)
mahasiswa3.bergabung_kelompok(kelompok1)
mahasiswa4.bergabung_kelompok(kelompok1)
mahasiswa5.bergabung_kelompok(kelompok1) # melebihi jumlah maksimal

kelompok1.daftar_mahasiswa()

mahasiswa3.keluar_kelompok()

kelompok1.daftar_mahasiswa()
