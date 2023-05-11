class PersegiPanjangMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luas(cls, panjang, lebar):
            return panjang * lebar
        cls.luas = classmethod(luas)
        def keliling(cls, panjang, lebar):
            return 2 * (panjang + lebar)
        cls.keliling = classmethod(keliling)

class PersegiPanjang(metaclass=PersegiPanjangMeta):
    pass
A = PersegiPanjang()
B = A.luas(4,5)
C = A.keliling(4,5)
print('Luas Persegi Panjang:',B)
print('Keliling Persegi panjang:',C)

print("=================================")

#Contoh 2:
class SegitigaMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung luas dan keliling segitiga
        def luas(cls, alas, tinggi):
            return (alas * tinggi) / 2
        cls.luas = classmethod(luas)
        def keliling(cls, sisi1, sisi2, sisi3):
            return sisi1 + sisi2 + sisi3
        cls.keliling = classmethod(keliling)

class Segitiga(metaclass=SegitigaMeta):
    pass
s = Segitiga()
# Menghitung luas segitiga dengan alas=4 dan tinggi=5
luas_segitiga = Segitiga.luas(4, 5)
print("Luas segitiga:", luas_segitiga)
# Menghitung keliling segitiga dengan sisi1=3, sisi2=4, dan sisi3=5
keliling_segitiga = Segitiga.keliling(3, 4, 5)
print("Keliling segitiga:", keliling_segitiga)