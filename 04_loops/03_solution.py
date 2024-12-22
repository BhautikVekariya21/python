def multiplication_table(number):
    for i in range(1, 11):  # Loop from 1 to 10 for the table
        if i == 5:  # Skip the fifth iteration
            continue
        print(f"{number} x {i} = {number * i}")

# Get input from the user
number = int(input("Enter a number for the multiplication table: "))

# Print the multiplication table but skip the fifth iteration
multiplication_table(number)
