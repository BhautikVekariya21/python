
# ----------------------------------------------
# Example Class with Class and Instance Methods
# ----------------------------------------------
class Example:
    class_variable = "Shared among all instances"

    def __init__(self, value):
        self.instance_variable = value  # Instance-specific data

    @classmethod
    def display_class_variable(cls):
        print(f"Class Variable: {cls.class_variable}")  # Access class-level data

    def display_instance_variable(self):
        print(f"Instance Variable: {self.instance_variable}")  # Access instance-level data

print("----- Example Class -----")
obj = Example(10)
obj.display_instance_variable()
Example.display_class_variable()

# ----------------------------------------------
# Basic Class and Object Example
# ----------------------------------------------
class Animal:
    # Constructor with default attributes
    def __init__(self, name, species):
        self.name = name  # Instance variable
        self.species = species  # Instance variable
    
    # Instance method
    def make_sound(self):
        return f"{self.name} makes a generic animal sound."
    
    # Class method
    @classmethod
    def from_string(cls, animal_str):
        name, species = animal_str.split(',')
        return cls(name.strip(), species.strip())
    
    # Static method
    @staticmethod
    def is_animal():
        return True

print("\n----- Animal Class -----")
# Creating an object of the Animal class
animal = Animal("Buddy", "Dog")
print(f"Animal Name: {animal.name}")
print(f"Animal Species: {animal.species}")
print(animal.make_sound())

# ----------------------------------------------
# Using class method to create an object
# ----------------------------------------------
print("\n----- Using Class Method -----")
animal2 = Animal.from_string("milo, Cat")
print(f"Animal2 Name: {animal2.name}")
print(f"Animal2 Species: {animal2.species}")
print(animal2.make_sound())

# ----------------------------------------------
# Checking static method
# ----------------------------------------------
print("\n----- Static Method Check -----")
print(f"Is it an animal? {Animal.is_animal()}")

# ----------------------------------------------
# Inheritance from a Superclass - Dog Class
# ----------------------------------------------
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call the superclass constructor
        self.breed = breed  # Additional attribute for the subclass
    
    # Overriding the make_sound method
    def make_sound(self):
        return f"{self.name} barks!"
    
    # New method specific to the Dog class
    def fetch(self, item):
        return f"{self.name} fetches the {item}."

print("\n----- Dog Class (Inheritance) -----")
# Creating an object of the Dog class
dog = Dog("Max", "Golden Retriever")
print(f"Dog Name: {dog.name}")
print(f"Dog Species: {dog.species}")
print(f"Dog Breed: {dog.breed}")
print(dog.make_sound())
print(dog.fetch("ball"))

# ----------------------------------------------
# Inheritance from a Superclass - Cat Class
# ----------------------------------------------
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")  # Call the superclass constructor
        self.color = color  # Additional attribute for the subclass
    
    # Overriding the make_sound method
    def make_sound(self):
        return f"{self.name} meows!"
    
    # New method specific to the Cat class
    def climb(self):
        return f"{self.name} climbs the tree."

print("\n----- Cat Class (Inheritance) -----")
# Creating an object of the Cat class
cat = Cat("Whiskers", "Black")
print(f"Cat Name: {cat.name}")
print(f"Cat Species: {cat.species}")
print(f"Cat Color: {cat.color}")
print(cat.make_sound())
print(cat.climb())

# End of Script
