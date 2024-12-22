def sum_of_two_numbers(num1, num2):
    """
    Takes two numbers as parameters and returns their sum.
    """
    try:
        # Convert the inputs to floats (if not already numbers)
        num1 = float(num1)
        num2 = float(num2)
        
        # Calculate the sum
        total = num1 + num2
        
        # Return the result
        return total
    except ValueError:
        # Handle invalid inputs
        return "Invalid input! Please provide valid numbers."

# Take inputs from the user
input1 = input("Enter the first number: ")
input2 = input("Enter the second number: ")

# Call the function with the user-provided inputs and display the result
result = sum_of_two_numbers(input1, input2)
print(f"The sum of the two numbers is: {result}")
