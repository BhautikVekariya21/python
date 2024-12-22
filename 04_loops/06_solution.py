def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):  # Loop from 1 to the given number (inclusive)
            result *= i  # Multiply the current result by the current number
        return result

# Get input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate and display the factorial
print(f"The factorial of {num} is: {factorial(num)}")

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1  # Initialize the result to 1
    counter = n  # Start the counter at the input number
    while counter > 0:  # Loop until the counter is greater than 0
        result *= counter  # Multiply the result by the counter
        counter -= 1  # Decrement the counter
    return result

# Get input from the user
num = int(input("Enter a number to calculate its factorial: "))

# Calculate and display the factorial
print(f"The factorial of {num} is: {factorial(num)}")

