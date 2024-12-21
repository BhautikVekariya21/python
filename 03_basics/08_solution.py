import re

def check_password_strength(password):
    """
    Function to check the strength of a password.
    """
    # Define the password strength criteria
    min_length = 8
    has_uppercase = re.compile(r'[A-Z]')
    has_lowercase = re.compile(r'[a-z]')
    has_digit = re.compile(r'[0-9]')
    has_special_char = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    # Check password length
    if len(password) < min_length:
        return "Weak: Password should be at least 8 characters long."

    # Check for uppercase letter
    if not has_uppercase.search(password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for lowercase letter
    if not has_lowercase.search(password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for digit
    if not has_digit.search(password):
        return "Weak: Password should contain at least one digit."

    # Check for special character
    if not has_special_char.search(password):
        return "Weak: Password should contain at least one special character."

    # If all conditions are met, it's a strong password
    if len(password) >= 12:
        return "Strong: Password is strong."

    # If it's long enough and meets the criteria but not very long
    return "Medium: Password is medium strength."

# Main program
def main():
    password = input("Enter your password to check its strength: ")
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()
