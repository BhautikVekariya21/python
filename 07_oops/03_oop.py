# fruit_example.py

# ------------------------------------------------------
# 1. Basic Class and Object
# ------------------------------------------------------
class Fruit:
    """
    A basic class to represent a fruit.
    Attributes:
        __name: The name of the fruit (private attribute).
        color: The color of the fruit.
    Methods:
        describe: Describes the fruit by its name and color.
        get_name: Returns the name of the fruit (getter method).
    """
    def __init__(self, name, color):
        """
        Constructor for the Fruit class.
        Initializes the name and color of the fruit.
        
        :param name: Name of the fruit (e.g., "Apple").
        :param color: Color of the fruit (e.g., "Red").
        """
        self.__name = name  # Private attribute for the name of the fruit
        self.color = color  # Public attribute for the color of the fruit

    def describe(self):
        """
        Describes the fruit by its name and color.
        
        :return: A string describing the fruit.
        """
        return f"The {self.__name} is {self.color}."

    def get_name(self):
        """
        Getter method to access the private name attribute.
        
        :return: The name of the fruit.
        """
        return self.__name

# ------------------------------------------------------
# 2. Polymorphism and Method Overriding
# ------------------------------------------------------
class Citrus(Fruit):
    """
    A subclass of Fruit to represent citrus fruits like lemons, oranges, etc.
    Adds an additional attribute for sourness and overrides the describe method.
    """
    def __init__(self, name, color, sourness):
        """
        Constructor for the Citrus class.
        
        :param name: Name of the citrus fruit (e.g., "Lemon").
        :param color: Color of the citrus fruit (e.g., "Yellow").
        :param sourness: The level of sourness in the citrus fruit (e.g., "High").
        """
        super().__init__(name, color)  # Call the parent constructor
        self.sourness = sourness  # Additional attribute specific to citrus fruits

    def describe(self):
        """
        Overriding the describe method to include sourness for citrus fruits.
        
        :return: A string describing the citrus fruit.
        """
        return f"The {self.get_name()} is {self.color} and has a sourness level of {self.sourness}."

class Berry(Fruit):
    """
    A subclass of Fruit to represent berry fruits like strawberries, blueberries, etc.
    Adds an additional attribute for sweetness and overrides the describe method.
    """
    def __init__(self, name, color, sweetness):
        """
        Constructor for the Berry class.
        
        :param name: Name of the berry fruit (e.g., "Strawberry").
        :param color: Color of the berry fruit (e.g., "Red").
        :param sweetness: The level of sweetness in the berry fruit (e.g., "Sweet").
        """
        super().__init__(name, color)  # Call the parent constructor
        self.sweetness = sweetness  # Additional attribute specific to berries

    def describe(self):
        """
        Overriding the describe method to include sweetness for berries.
        
        :return: A string describing the berry fruit.
        """
        return f"The {self.get_name()} is {self.color} and has a sweetness level of {self.sweetness}."

# ------------------------------------------------------
# 3. Method Overloading (Simulated)
# ------------------------------------------------------
class FruitWithOverloading(Fruit):
    """
    A subclass of Fruit that simulates method overloading for the describe method.
    Based on the argument passed, it provides different descriptions.
    """
    def __init__(self, name, color):
        """
        Constructor for the FruitWithOverloading class.
        
        :param name: Name of the fruit (e.g., "Apple").
        :param color: Color of the fruit (e.g., "Green").
        """
        super().__init__(name, color)  # Call the parent constructor

    def describe(self, description_type="basic"):
        """
        Simulates method overloading by providing different descriptions based on the description_type.
        
        :param description_type: The type of description ("basic" or "detailed").
        :return: A string describing the fruit in different ways.
        """
        if description_type == "basic":
            return f"The {self.get_name()} is {self.color}."  # Basic description
        elif description_type == "detailed":
            return f"The {self.get_name()} is {self.color}, and it has a rich flavor profile."  # Detailed description
        else:
            return f"The {self.get_name()} description is not available."  # For unknown types

# ------------------------------------------------------
# 4. Creating Objects and Demonstrating Polymorphism, Method Overriding, and Overloading
# ------------------------------------------------------

# Creating instances of the subclasses
lemon = Citrus("Lemon", "Yellow", "High")  # Citrus object
strawberry = Berry("Strawberry", "Red", "Sweet")  # Berry object
apple = FruitWithOverloading("Apple", "Green")  # FruitWithOverloading object

# Demonstrating Polymorphism: Calling the same method on different objects
print("------------------------------------------------------")
print("2. Polymorphism and Method Overriding")
print(lemon.describe())  # Method overridden in Citrus class
print(strawberry.describe())  # Method overridden in Berry class
print(apple.describe("detailed"))  # Using overloaded method in FruitWithOverloading
print("------------------------------------------------------")

# ------------------------------------------------------
# 5. Encapsulation (Getter Method)
# ------------------------------------------------------
orange = Fruit("Orange", "Orange")  # Creating a basic fruit object
print("------------------------------------------------------")
print("5. Encapsulation")
print(f"Fruit Name (using getter): {orange.get_name()}, Color: {orange.color}")
print("------------------------------------------------------")
