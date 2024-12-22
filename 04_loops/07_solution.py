def get_valid_number():
    while True:  # Keep looping until a valid input is provided
        try:
            num = int(input("Enter a number between 1 and 1123: "))
            if 1 <= num <= 1123:
                return num  # Valid input, return the number
            else:
                print("Invalid input. Please enter a number between 1 and 1123.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Call the function and display the result
valid_number = get_valid_number()
print(f"You entered a valid number: {valid_number}")
