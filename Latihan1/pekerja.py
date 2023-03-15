class Pekerja:
    def __init__(self, nama, nopk):
        self.nama = nama
        self.nopk = nopk
    
    def info(self):
        print(f"Nama: {self.nama}\nNOPK: {self.nopk}")
    
pekerjaA = Pekerja("Wahyudi", "40785643")
pekerjaA.info()
pekerjaB = Pekerja("Suparto", "50784321")
pekerjaB.info()