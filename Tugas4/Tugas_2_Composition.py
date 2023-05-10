class Hewan:
    def __init__(self, nama, jenis_hewan):
        self.nama = nama
        self.jenis_hewan = jenis_hewan

    def info(self):
        print(f"Nama hewan: {self.nama}")
        self.jenis_hewan.info()

class JenisHewan:
    def __init__(self, nama_jenis, habitat):
        self.nama_jenis = nama_jenis
        self.habitat = habitat

    def info(self):
        print(f"Jenis hewan: {self.nama_jenis}")
        print(f"Habitat: {self.habitat}")

# Contoh penggunaan
jenis1 = JenisHewan("Gajah", "Hutan dan padang rumput")
jenis2 = JenisHewan("Singa", "Savana")

hewan1 = Hewan("Hutan", jenis1)
hewan2 = Hewan("Simba", jenis2)

hewan1.info()
hewan2.info()
