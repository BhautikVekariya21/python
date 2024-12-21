
# Integer data type
num1 = 10
num2 = -20

# Float data type 
float1 = 3.14
float2 = -0.001

# Complex number
complex1 = 3 + 4j
complex2 = 2 - 3j

# Number type methods
# abs() - returns absolute value
abs_value = abs(-10)  # Returns 10

# round() - rounds number to specified decimals
rounded = round(3.14159, 2)  # Returns 3.14

# pow() - returns x to power y
power = pow(2, 3)  # Returns 8

# max() and min()
maximum = max(10, 20, 30)  # Returns 30
minimum = min(10, 20, 30)  # Returns 10

# Type conversion
# Convert to int
int_num = int(3.14)  # Returns 3
int_str = int("10")  # Returns 10

# Convert to float
float_num = float(5)  # Returns 5.0
float_str = float("3.14")  # Returns 3.14

# Convert to complex
complex_num = complex(2, 3)  # Returns 2+3j

# Number system conversion
# Binary to int
bin_to_int = int('1010', 2)  # Returns 10

# Octal to int 
oct_to_int = int('12', 8)  # Returns 10

# Hex to int
hex_to_int = int('A', 16)  # Returns 10

# Math operations
sum_nums = 10 + 5  # Addition
diff = 10 - 5  # Subtraction
product = 10 * 5  # Multiplication
quotient = 10 / 5  # Division
floor_div = 10 // 3  # Floor division
modulus = 10 % 3  # Modulus
exponent = 10 ** 2  # Exponentiation
# Print all number values and results
print("Integer values:")
print(f"num1 = {num1}")
print(f"num2 = {num2}")

print("\nFloat values:")
print(f"float1 = {float1}")
print(f"float2 = {float2}")

print("\nComplex values:")
print(f"complex1 = {complex1}")
print(f"complex2 = {complex2}")

print("\nNumber methods results:")
print(f"abs_value = {abs_value}")
print(f"rounded = {rounded}")
print(f"power = {power}")
print(f"maximum = {maximum}")
print(f"minimum = {minimum}")

print("\nType conversion results:")
print(f"int_num = {int_num}")
print(f"int_str = {int_str}")
print(f"float_num = {float_num}")
print(f"float_str = {float_str}")
print(f"complex_num = {complex_num}")

print("\nNumber system conversion results:")
print(f"bin_to_int = {bin_to_int}")
print(f"oct_to_int = {oct_to_int}")
print(f"hex_to_int = {hex_to_int}")

print("\nMath operation results:")
print(f"sum_nums = {sum_nums}")
print(f"diff = {diff}")
print(f"product = {product}")
print(f"quotient = {quotient}")
print(f"floor_div = {floor_div}")
print(f"modulus = {modulus}")
print(f"exponent = {exponent}")