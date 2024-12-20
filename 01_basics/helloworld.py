def get_user_info():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    return name, age

def calculate_birth_year(age):
    current_year = 2024
    birth_year = current_year - age
    return birth_year

def print_user_info(name, birth_year):
    print(f"Hello {name}! Nice to meet you.")
    print(f"You were born in {birth_year}.")

def get_numbers():
    print("\nLet's do some basic math!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return num1, num2

def calculate_operations(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division

def print_results(num1, num2, addition, subtraction, multiplication, division):
    print(f"\nResults:")
    print(f"{num1} + {num2} = {addition}")
    print(f"{num1} - {num2} = {subtraction}")
    print(f"{num1} * {num2} = {multiplication}")
    print(f"{num1} / {num2} = {division}")

def main():
    name, age = get_user_info()
    birth_year = calculate_birth_year(age)
    print_user_info(name, birth_year)
    
    num1, num2 = get_numbers()
    addition, subtraction, multiplication, division = calculate_operations(num1, num2)
    print_results(num1, num2, addition, subtraction, multiplication, division)

if __name__ == "__main__":
    main()