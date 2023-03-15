class Persegi:
    def __init__(self, panjang, lebar):       
        self.panjang = panjang
        self.lebar = lebar
    def luas(self):
        return self.panjang*self.lebar
persegiA = Persegi(29,30)
print(f"luas Persegi: {persegiA.luas()}")