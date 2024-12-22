def first_non_repeated_character(string):
    for char in string:
        if string.count(char) == 1:  # Check if the count of the character is 1
            return char
    return None  # Return None if no non-repeated character is found

# Get input from the user
user_input = input("Enter a string: ")

# Find the first non-repeated character
result = first_non_repeated_character(user_input)

if result is not None:
    print(f"The first non-repeated character is: {result}")
else:
    print("There is no non-repeated character in the string.")
