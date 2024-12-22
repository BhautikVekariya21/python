def sum_of_even_numbers(n):
    sum_even = 0
    for num in range(2, n + 1, 2):  # Start from 2 and increment by 2 to get even numbers
        sum_even += num
    return sum_even

# Get input from the user
n = int(input("Enter a number (n): "))

# Calculate the sum of even numbers up to n
result = sum_of_even_numbers(n)

print(f"The sum of even numbers up to {n} is: {result}")
