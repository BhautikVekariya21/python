def check_uniqueness(lst):
    # Convert the list to a set and compare its length with the original list
    if len(lst) == len(set(lst)):
        return True  # All elements are unique
    else:
        return False  # There are duplicates

# Get input from the user
user_list = input("Enter a list of items separated by spaces: ").split()

# Check if the list has unique elements
if check_uniqueness(user_list):
    print("The list has all unique elements.")
else:
    print("The list has duplicate elements.")
