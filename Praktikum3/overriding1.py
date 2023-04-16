#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

class Marvel:
    def help(self):
        print("Marvel in here")

class IronMan(Marvel):
    def help(self):
        print("IronMan is helping you")

class Spiderman(Marvel):
    def help(self):
        print("Spiderman in dark is coming to you")

class Piterparker(Spiderman):
    def help(self):
        print("Piterparker akan melawan venom")

class Tonystark(IronMan):
    def help(self):
        print("Tony Stark akan membasmi Thanos dan teman-temannya")

def marvel_help(marvel):
    marvel.help()

marvel = Marvel()
darmen = Spiderman()
iron = IronMan()
orang1 = Piterparker()
orang2 = Tonystark()

marvel_help(marvel)
marvel_help(darmen)
marvel_help(iron)
marvel_help(orang1)
marvel_help(orang2)