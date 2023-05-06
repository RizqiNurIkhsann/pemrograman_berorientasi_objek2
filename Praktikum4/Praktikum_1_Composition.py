class Jurnal:
    def __init__(self, judul, tahun, penulis):
        self.judul = judul
        self.tahun = tahun
        self.penulis = penulis

class Peneliti:
    def __init__(self, nama, institusi):
        self.nama = nama
        self.institusi = institusi
        self.jurnals = []

    def tambah_jurnal(self, jurnal):
        self.jurnals.append(jurnal)

    def daftar_jurnal(self):
        print(f"Daftar Jurnal dari {self.nama} ({self.institusi}):")
        for jurnal in self.jurnals:
            print(f"- {jurnal.judul} ({jurnal.tahun}), oleh {jurnal.penulis}")

# Contoh penggunaan
jurnal1 = Jurnal("Pengaruh Polusi Udara terhadap Kesehatan", 2022, "Dr. A. Setiawan")
jurnal2 = Jurnal("Pemanfaatan Energi Matahari untuk Pertanian", 2023, "Dr. B. Siregar")

peneliti1 = Peneliti("Prof. C. Kusuma", "Universitas XYZ")
peneliti1.tambah_jurnal(jurnal1)
peneliti1.tambah_jurnal(jurnal2)

peneliti1.daftar_jurnal()