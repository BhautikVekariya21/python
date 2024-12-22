def multiply(a, b):
    """
    Multiplies two inputs.
    If both inputs are numbers, returns their product.
    If one input is a string and the other is an integer, repeats the string.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # Both inputs are numbers
        return a * b
    elif isinstance(a, str) and isinstance(b, int):
        # First input is a string, second input is an integer
        return a * b
    elif isinstance(a, int) and isinstance(b, str):
        # First input is an integer, second input is a string
        return b * a
    else:
        # Handle invalid combinations
        return "Invalid inputs: Provide two numbers or a string and an integer."

# Get input from the user
input1 = input("Enter the first value (number or string): ")
input2 = input("Enter the second value (number or string): ")

# Convert inputs to appropriate types
if input1.isdigit():
    input1 = int(input1)
elif input1.replace('.', '', 1).isdigit():
    input1 = float(input1)

if input2.isdigit():
    input2 = int(input2)
elif input2.replace('.', '', 1).isdigit():
    input2 = float(input2)

# Call the function and display the result
result = multiply(input1, input2)
print(f"Result: {result}")
