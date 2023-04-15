class Animal:
    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

def animal_sound(animal):
    animal.make_sound()

# Instantiate objects of each class
animal = Animal()
dog = Dog()
cat = Cat()

# Call the animal_sound function for each object
animal_sound(animal) # Output: The animal makes a sound
animal_sound(dog) # Output: The dog barks
animal_sound(cat) # Output: The cat meows