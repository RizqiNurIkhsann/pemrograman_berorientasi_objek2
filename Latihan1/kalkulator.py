class kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('tidak dapat membagi nol!')
        return x / y 
    
    @staticmethod
    def mod(x, y):
        return x % y
    
    @staticmethod
    def floordivision(x, y):
        return x // y
    
print(f'Pertambahan\t= {kalkulator.add(3,3)}')
print(f'Pengurangan\t= {kalkulator.subtract(8,3)}')
print(f'Perkalian\t= {kalkulator.multiply(7,9)}')
print(f'Pembagian\t= {kalkulator.divide(7,10)}')
print(f'Modulus\t\t= {kalkulator.mod(9,80)}')
print(f'Floor Division\t= {kalkulator.floordivision(15,11)}')