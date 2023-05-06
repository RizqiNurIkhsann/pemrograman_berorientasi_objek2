class Penulis:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.buku = []

    def tambah_buku(self, buku):
        self.buku.append(buku)

    def daftar_buku(self):
        print(f"Daftar buku oleh penulis {self.nama}:")
        for buku in self.buku:
            print(f"- {buku.judul}")

class Buku:
    def __init__(self, judul, tahun_terbit, penulis):
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penulis = penulis
        penulis.tambah_buku(self)

# Contoh penggunaan
penulis1 = Penulis("Agatha Christie", "Inggris")

buku1 = Buku("Murder on the Orient Express", 1934, penulis1)
buku2 = Buku("And Then There Were None", 1939, penulis1)
buku3 = Buku("The Murder of Roger Ackroyd", 1926, penulis1)

penulis1.daftar_buku()
