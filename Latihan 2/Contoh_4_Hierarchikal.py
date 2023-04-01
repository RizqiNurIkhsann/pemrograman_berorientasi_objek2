class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color


class TwoDimensional(Shape):
    def __init__(self, name, color, sides):
        super().__init__(name, color)
        self.sides = sides
        
    def get_sides(self):
        return self.sides


class ThreeDimensional(Shape):
    def __init__(self, name, color, dimensions):
        super().__init__(name, color)
        self.dimensions = dimensions
        
    def get_dimensions(self):
        return self.dimensions


class Sphere(ThreeDimensional):
    def __init__(self, name, color, dimensions, radius):
        super().__init__(name, color, dimensions)
        self.radius = radius
        
    def get_radius(self):
        return self.radius


twodimensional = TwoDimensional("Kubus", "Biru", 8)
print("Name:",twodimensional.get_name())
print("Color:",twodimensional.get_color())
print("Sides:",twodimensional.get_sides())
print("=============================")
threedimensional = ThreeDimensional("Bulat", "Hitam", "3D")
print("Name:",threedimensional.get_name())
print("Color:",threedimensional.get_color())
print("Dimensions:",threedimensional.get_dimensions())
print("=============================")
sphere = Sphere("Sphere", "Hijau", "3D", 30)
print("Name:",sphere.get_name())
print("Color:",sphere.get_color())
print("Dimensions:",sphere.get_dimensions())
print("Radius:",sphere.get_radius())