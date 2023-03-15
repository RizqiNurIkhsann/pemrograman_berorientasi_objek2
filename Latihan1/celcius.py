class celcius:
    @staticmethod
    def fahrenhait(celcius):
        return (celcius * 9/5) + 32
    @staticmethod
    def kelvin(celcius):
        return celcius + 273.15
    @staticmethod
    def reamur (celcius):
        return celcius * 4/5

brpcelcius = 80
fahrenhait = celcius.fahrenhait(brpcelcius)
kelvin = celcius.kelvin(brpcelcius)
reamur = celcius.reamur(brpcelcius)

print(f'29 celcius ke\t: fahrenhait\t: {fahrenhait}, kelvin\t\t: {kelvin}, reamur\t\t: {reamur}')