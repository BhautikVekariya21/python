def generate_even_numbers(limit, use_yield=True):
    if use_yield:
        # Using yield to generate even numbers (generator function)
        num = 2
        while num <= limit:
            yield num
            num += 2
    else:
        # Without yield (returns a list of even numbers)
        even_numbers = []
        num = 2
        while num <= limit:
            even_numbers.append(num)
            num += 2
        return even_numbers

# Example usage with yield
print("Using yield:")
even_gen = generate_even_numbers(20, use_yield=True)  # Using generator
for even in even_gen:
    print(even)

# Example usage without yield (returns a list)
print("\nWithout yield:")
even_list = generate_even_numbers(20, use_yield=False)  # Without generator
print(even_list)
