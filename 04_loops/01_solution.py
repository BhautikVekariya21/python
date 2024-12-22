def count_positive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

# Get a list of numbers from the user
user_input = input("Enter numbers separated by space: ")

# Convert the input string to a list of integers
numbers = list(map(int, user_input.split()))

# Calculate the number of positive numbers
positive_count = count_positive_numbers(numbers)

print(f"The number of positive numbers in the list is: {positive_count}")
