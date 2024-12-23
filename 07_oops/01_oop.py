
# ----------------------------------------------
# Example Class Demonstrating `self` and `cls`
# ----------------------------------------------

class Example:
    # Class-level attribute (shared by all instances)
    class_variable = "Shared among all instances"

    def __init__(self, value):
        # `self` is used to initialize instance-specific attributes
        self.instance_variable = value

    # Instance method: uses `self` to access instance-specific data
    def display_instance_variable(self):
        print(f"Instance Variable: {self.instance_variable}")  # Accessing instance attribute via `self`

    # Class method: uses `cls` to access or modify class-level data
    @classmethod
    def display_class_variable(cls):
        print(f"Class Variable: {cls.class_variable}")  # Accessing class-level attribute via `cls`

    # Class method: modifies the class-level attribute
    @classmethod
    def change_class_variable(cls, new_value):
        cls.class_variable = new_value  # Modifying class-level attribute via `cls`

print("----- Example Class -----")
# Creating instances
obj1 = Example(10)
obj2 = Example(20)

# Demonstrating `self` with instance methods
obj1.display_instance_variable()  # Output: Instance Variable: 10
obj2.display_instance_variable()  # Output: Instance Variable: 20

# Demonstrating `cls` with class methods
Example.display_class_variable()  # Output: Class Variable: Shared among all instances
Example.change_class_variable("Updated class variable")
Example.display_class_variable()  # Output: Class Variable: Updated class variable

# ----------------------------------------------
# Key Difference Between `self` and `cls`
# ----------------------------------------------
# `self` refers to the instance of the class, allowing access to instance-specific attributes.
# `cls` refers to the class itself, allowing access to or modification of class-level attributes.

# ----------------------------------------------
# Basic Class and Object Example
# ----------------------------------------------

class Animal:
    # Constructor with default attributes
    def __init__(self, name, species):
        self.name = name  # Instance variable
        self.species = species  # Instance variable
    
    # Instance method: uses `self` to access instance-specific data
    def make_sound(self):
        return f"{self.name} makes a generic animal sound."
    
    # Class method: uses `cls` to create an instance from a string
    @classmethod
    def from_string(cls, animal_str):
        name, species = animal_str.split(',')
        return cls(name.strip(), species.strip())
    
    # Static method: doesn't use `self` or `cls` because it doesn't depend on instance or class
    @staticmethod
    def is_animal():
        return True

print("\n----- Animal Class -----")
# Creating an object of the Animal class
animal = Animal("Buddy", "Dog")
print(f"Animal Name: {animal.name}")
print(f"Animal Species: {animal.species}")
print(animal.make_sound())

# Using class method to create an object
print("\n----- Using Class Method -----")
animal2 = Animal.from_string("Charlie, Cat")
print(f"Animal2 Name: {animal2.name}")
print(f"Animal2 Species: {animal2.species}")
print(animal2.make_sound())

# Checking static method
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
