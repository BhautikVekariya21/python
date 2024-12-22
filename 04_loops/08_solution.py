def is_prime(num):
    if num <= 1:  # Prime numbers are greater than 1
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisors up to the square root of num
        if num % i == 0:  # If divisible, it's not a prime
            return False
    return True  # If no divisors found, it's a prime

# Get input from the user
try:
    number = int(input("Enter a number to check if it's prime: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")
