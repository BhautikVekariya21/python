def motivational_message(name="Friend"):
    """
    Prints a motivational message with the given name.
    If no name is provided, uses the default name 'Friend'.
    """
    message = f"Hey {name}, keep pushing forward! You are capable of amazing things. 🌟"
    print(message)

# Input from user
user_name = input("Enter your name (or press Enter to use the default): ").strip()

# Call the function
if user_name:
    motivational_message(user_name)
else:
    motivational_message()
