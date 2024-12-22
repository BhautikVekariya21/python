# Lambda functions
perimeter = lambda length, width: 2 * (length + width)
circumference = lambda length, width: 2 * (length + width)  # Same as perimeter for a rectangle
diagonal = lambda length, width: (length**2 + width**2) ** 0.5

# Input from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Compute results
rect_perimeter = perimeter(length, width)
rect_circumference = circumference(length, width)
rect_diagonal = diagonal(length, width)

# Output the results
print(f"\nResults for the rectangle with length {length} and width {width}:")
print(f"Perimeter: {rect_perimeter}")
print(f"Circumference: {rect_circumference}")
print(f"Diagonal: {rect_diagonal:.2f}")

# Product list with price and category
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Shirt", "price": 50, "category": "clothing"},
    {"name": "Watch", "price": 150, "category": "electronics"},
    {"name": "Shoes", "price": 80, "category": "clothing"},
    {"name": "Book", "price": 20, "category": "books"}  # No discount for "books"
]

# Discount logic
discounts = {
    "electronics": lambda price: price * 0.9,  # 10% discount for electronics
    "clothing": lambda price: price * 0.8      # 20% discount for clothing
}

# Apply discounts to each product
for product in products:
    discount = discounts.get(product["category"], lambda price: price)  # Default no discount
    product["final_price"] = discount(product["price"])

# Print final prices
for product in products:
    print(f"{product['name']} - Final Price: ${product['final_price']:.2f}")
