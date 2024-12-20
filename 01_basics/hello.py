from helloworld import get_user_info, calculate_birth_year, print_user_info, get_numbers, calculate_operations, print_results

def greet_user(name):
    from datetime import datetime
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print(f"{greeting}, {name}!")

def main():
    # Use imported functions
    name, age = get_user_info()
    birth_year = calculate_birth_year(age)
    print_user_info(name, birth_year)
    
    num1, num2 = get_numbers()
    addition, subtraction, multiplication, division = calculate_operations(num1, num2)
    print_results(num1, num2, addition, subtraction, multiplication, division)

    # Additional functionality: Greet user based on the time of day
    greet_user(name)

if __name__ == "__main__":
    main()
