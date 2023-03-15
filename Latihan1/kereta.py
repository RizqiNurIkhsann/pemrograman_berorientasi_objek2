class KeretaApi:
    def __init__(self, maskapai, tujuan, kodekeberangkatan):
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.kodepenerbangan = kodekeberangkatan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}\nKode Keberangkatan: {self.kodepenerbangan}")
keretaA = KeretaApi("Argo Sindoro", "CRB - GBR", "012111e2125")
keretaA.info()
