#Nama   : Muhammad Rizqi Nur Ikhsannudin
#Nim    : 210511100
#Kelas  : R3/TIF21C 

# Single Inheritance
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Single Inheritance
class Drawable:
    def draw(self):
        print("Drawing object at: ", self.x, self.y)

# Single Inheritance
class Moveable:
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

# Multiple Inheritance
class Player(GameObject, Drawable, Moveable):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def update(self):
        self.move(5, 9)
        self.draw()

player = Player(3, 6)
player.update()