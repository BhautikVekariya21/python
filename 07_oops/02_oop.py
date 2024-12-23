# fruit_example.py

# ------------------------------------------------------
# 1. Basic Class and Object
# ------------------------------------------------------
# This example demonstrates the creation of a basic class with attributes.
# An instance of the class is created, and its attributes are accessed.
class Fruit:
    def __init__(self, name, color):
        """
        Constructor for the Fruit class.
        :param name: Name of the fruit
        :param color: Color of the fruit
        """
        self.name = name  # Instance attribute for fruit name
        self.color = color  # Instance attribute for fruit color

# Creating an instance of the Fruit class
apple = Fruit("Apple", "Red")
print("------------------------------------------------------")
print("1. Basic Class and Object")
print(f"Fruit: {apple.name}, Color: {apple.color}")
print("------------------------------------------------------")

# ------------------------------------------------------
# 2. Class Method and Self
# ------------------------------------------------------
# This example demonstrates how to use `self` to access instance-specific
# data. It adds a method that describes the fruit.
class Fruit:
    def __init__(self, name, color):
        """
        Constructor for the Fruit class.
        :param name: Name of the fruit
        :param color: Color of the fruit
        """
        self.name = name
        self.color = color

    def describe(self):
        """
        Instance method to describe the fruit.
        :return: A string describing the fruit
        """
        return f"The {self.name} is {self.color}."

# Creating an instance of the Fruit class
banana = Fruit("Banana", "Yellow")
print("------------------------------------------------------")
print("2. Class Method and Self")
print(banana.describe())
print("------------------------------------------------------")

# ------------------------------------------------------
# 3. Inheritance
# ------------------------------------------------------
# This example demonstrates inheritance by creating a subclass `Citrus`.
# The subclass inherits attributes from the parent class and adds its own.
class Citrus(Fruit):
    def __init__(self, name, color, sourness):
        """
        Constructor for the Citrus class.
        :param name: Name of the citrus fruit
        :param color: Color of the citrus fruit
        :param sourness: Level of sourness of the citrus fruit
        """
        super().__init__(name, color)  # Call the parent class constructor
        self.sourness = sourness  # Additional attribute for sourness

    def describe_citrus(self):
        """
        Method to describe the citrus fruit.
        :return: A string describing the citrus fruit
        """
        return f"The {self.name} is {self.color} and has a sourness level of {self.sourness}."

# Creating an instance of the Citrus class
lemon = Citrus("Lemon", "Yellow", "High")
print("------------------------------------------------------")
print("3. Inheritance")
print(lemon.describe_citrus())
print("------------------------------------------------------")

# ------------------------------------------------------
# 4. Encapsulation
# ------------------------------------------------------
# This example demonstrates encapsulation by making an attribute private
# and providing a getter method to access it.
class Fruit:
    def __init__(self, name, color):
        """
        Constructor for the Fruit class.
        :param name: Name of the fruit
        :param color: Color of the fruit
        """
        self.__name = name  # Private attribute for fruit name
        self.color = color  # Public attribute for fruit color

    def get_name(self):
        """
        Getter method to access the private name attribute.
        :return: The name of the fruit
        """
        return self.__name

# Creating an instance of the Fruit class
orange = Fruit("Orange", "Orange")
print("------------------------------------------------------")
print("4. Encapsulation")
print(f"Fruit Name (using getter): {orange.get_name()}, Color: {orange.color}")
print("------------------------------------------------------")
