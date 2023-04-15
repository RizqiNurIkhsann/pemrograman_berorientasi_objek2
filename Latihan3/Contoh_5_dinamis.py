class Kucing:
    def bersuara(self):
        print("Meow")
class Anjing:
    def bersuara(self):
        print("Guk guk")
def cetak_suara(objek):
    objek.bersuara()

kucing = Kucing()
anjing = Anjing()
cetak_suara(kucing) # Output: Meow
cetak_suara(anjing) # Output: Guk guk