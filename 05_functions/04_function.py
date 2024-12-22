import math

def circle_properties(radius):
    """
    Calculate and return the area, perimeter, diameter, and circumference of a circle.
    
    Parameters:
        radius (float): The radius of the circle.
    
    Returns:
        tuple: A tuple containing the area, perimeter (circumference), diameter, and circumference.
    """
    if radius <= 0:
        return "Radius must be a positive number."
    
    # Calculations
    area = math.pi * radius ** 2  # Area of the circle
    circumference = 2 * math.pi * radius  # Circumference of the circle
    diameter = 2 * radius  # Diameter of the circle
    
    return area, circumference, diameter

# Input from user
radius = float(input("Enter the radius of the circle: "))

# Get the properties
properties = circle_properties(radius)

if isinstance(properties, str):
    print(properties)  # Error message if radius is invalid
else:
    # Unpack and display results
    area, circumference, diameter = properties
    print(f"Area: {area:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Diameter: {diameter:.2f}")
