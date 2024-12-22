def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

# Get input from the user
user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(user_input)

print(f"Reversed string: {reversed_string}")

def reverse_string(string):
    return string[::-1]

# Get input from the user
user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(user_input)

print(f"Reversed string: {reversed_string}")

def reverse_string(string):
    return ''.join(reversed(string))

# Get input from the user
user_input = input("Enter a string to reverse: ")
reversed_string = reverse_string(user_input)

print(f"Reversed string: {reversed_string}")
