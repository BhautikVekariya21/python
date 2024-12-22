def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Example usage:
result = sum_numbers(10, 20, 30, 40)
print("Sum of numbers:", result)

def calculate_average(*args):
    if len(args) == 0:
        return "No numbers provided"
    return sum(args) / len(args)

# Example usage:
average = calculate_average(10, 20, 30, 40, 50)
print("Average:", average)

def concatenate_strings(*args):
    return " ".join(args)

# Example usage:
result = concatenate_strings("Hello", "world", "from", "Python")
print(result)
