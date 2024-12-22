def square_of_number():
    """
    Prompts the user to input a number, calculates its square, and returns the result.
    """
    try:
        # Take input from the user and convert it to a float
        num = float(input("Enter a number: "))
        
        # Calculate the square of the number
        square = num ** 2
        
        # Return the square of the number
        return square
    except ValueError:
        # Handle invalid input
        return "Invalid input! Please enter a valid number."

# Call the function and display the result
result = square_of_number()
print(f"The square of the entered number is: {result}")
