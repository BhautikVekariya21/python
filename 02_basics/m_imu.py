
# Mutable Data Types Examples
# Lists are mutable - can be modified after creation
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying element
my_list.append(4) # Adding element
print(f"Modified list: {my_list}")  # [10, 2, 3, 4]

# Dictionaries are mutable
my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26  # Modifying value
my_dict['city'] = 'New York'  # Adding new key-value
print(f"Modified dict: {my_dict}")  # {'name': 'John', 'age': 26, 'city': 'New York'}

# Sets are mutable
my_set = {1, 2, 3}
my_set.add(4)  # Adding element
my_set.remove(1)  # Removing element
print(f"Modified set: {my_set}")  # {2, 3, 4}

# Immutable Data Types Examples
# Strings are immutable
my_string = "Hello"
new_string = my_string + " World"  # Creates new string
print(f"Original string: {my_string}")  # Hello
print(f"New string: {new_string}")  # Hello World

# Tuples are immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise TypeError
print(f"Tuple: {my_tuple}")  # (1, 2, 3)

# Numbers (int, float) are immutable
x = 5
y = x  # Creates new reference
x = 10  # Creates new object
print(f"x: {x}, y: {y}")  # x: 10, y: 5