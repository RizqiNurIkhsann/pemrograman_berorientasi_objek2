class Mobil:
    def __init__(self, nomor_plat, jenis_mobil):
        self.nomor_plat = nomor_plat
        self.jenis_mobil = jenis_mobil

    def info(self):
        print(f"Nomor plat: {self.nomor_plat}")
        self.jenis_mobil.info()

class JenisMobil:
    def __init__(self, merk, model, harga):
        self.merk = merk
        self.model = model
        self.harga = harga

    def info(self):
        print(f"Jenis mobil: {self.merk} {self.model}")
        print(f"Harga: {self.harga:,}")

# Contoh penggunaan
jenis1 = JenisMobil("Toyota", "Avanza", 200_000_000)
jenis2 = JenisMobil("Honda", "Jazz", 250_000_000)

mobil1 = Mobil("B 1234 CD", jenis1)
mobil2 = Mobil("B 5678 EF", jenis2)

mobil1.info()
mobil2.info()