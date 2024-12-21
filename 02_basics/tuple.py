
# Creating a simple tuple of fruits
fruits = ('apple', 'banana', 'orange', 'mango')

# Accessing tuple elements
# Tuples use zero-based indexing like lists
print(fruits[0])  # Prints: apple
print(fruits[-1]) # Prints: mango

# Tuple slicing
print(fruits[1:3])  # Prints: ('banana', 'orange')

# Creating a nested tuple
nested_fruits = (('apple', 'pear'), ('orange', 'mango'), ('grape', 'kiwi'))

# Accessing nested tuple elements
print(nested_fruits[0][1])  # Prints: pear

# Tuple operations
# Count method
fruit_count = fruits.count('apple')  # Returns number of times 'apple' appears

# Index method
banana_index = fruits.index('banana')  # Returns index of 'banana'

# Tuple concatenation
more_fruits = fruits + ('grape', 'kiwi')

# Comparing Tuple vs List
# List example - Mutable (can be changed)
fruit_list = ['apple', 'banana', 'orange']
fruit_list[0] = 'pear'  # Valid - lists can be modified

# Tuple example - Immutable (cannot be changed)
fruit_tuple = ('apple', 'banana', 'orange')
# fruit_tuple[0] = 'pear'  # This would raise an error

# Memory comparison
import sys
print(sys.getsizeof(fruit_list))    # Lists take more memory
print(sys.getsizeof(fruit_tuple))   # Tuples take less memory

# Speed comparison
# Tuples are generally faster than lists for iteration
for fruit in fruit_tuple:  # Faster
    pass

for fruit in fruit_list:   # Slightly slower
    pass
# Comparing more operations between lists and tuples

# Creation comparison
list_creation = ['a', 'b', 'c'] * 1000  # Creates list with repeated elements
tuple_creation = ('a', 'b', 'c') * 1000  # Creates tuple with repeated elements

# Length comparison 
list_len = len(['a', 'b', 'c'])  # Get length of list
tuple_len = len(('a', 'b', 'c'))  # Get length of tuple

# Membership testing
list_test = 'a' in ['a', 'b', 'c']  # Check if element exists in list
tuple_test = 'a' in ('a', 'b', 'c')  # Check if element exists in tuple

# Unpacking
list_a, list_b, list_c = [1, 2, 3]  # List unpacking
tuple_a, tuple_b, tuple_c = (1, 2, 3)  # Tuple unpacking

# Max and min operations
list_max = max([1, 2, 3])  # Find maximum in list
tuple_max = max((1, 2, 3))  # Find maximum in tuple

list_min = min([1, 2, 3])  # Find minimum in list 
tuple_min = min((1, 2, 3))  # Find minimum in tuple

# Sorting
sorted_list = sorted([3, 1, 2])  # Returns new sorted list
sorted_tuple = sorted((3, 1, 2))  # Returns new sorted list from tuple

# Reversing
reversed_list = list(reversed([1, 2, 3]))  # Returns iterator, convert to list
reversed_tuple = tuple(reversed((1, 2, 3)))  # Returns iterator, convert to tuple

# List specific operations (not possible with tuples)
my_list = [1, 2, 3]
my_list.append(4)  # Add element
my_list.extend([5, 6])  # Add multiple elements
my_list.insert(0, 0)  # Insert at specific position
my_list.remove(3)  # Remove specific element
my_list.pop()  # Remove and return last element
my_list.clear()  # Remove all elements
# Creating a simple tuple of fruits
fruits = ('apple', 'banana', 'orange', 'mango')
print(fruits[0])  # Output: apple
print(fruits[-1]) # Output: mango
print(fruits[1:3])  # Output: ('banana', 'orange')

# Creating a nested tuple
nested_fruits = (('apple', 'pear'), ('orange', 'mango'), ('grape', 'kiwi'))
print(nested_fruits[0][1])  # Output: pear

# Tuple operations
fruit_count = fruits.count('apple')  
print(f"Count of 'apple': {fruit_count}")  # Output: Count of 'apple': 1

banana_index = fruits.index('banana')
print(f"Index of 'banana': {banana_index}")  # Output: Index of 'banana': 1

more_fruits = fruits + ('grape', 'kiwi')
print(f"Concatenated tuple: {more_fruits}")  # Output: Concatenated tuple: ('apple', 'banana', 'orange', 'mango', 'grape', 'kiwi')

# Memory comparison
import sys
fruit_list = ['apple', 'banana', 'orange']
fruit_tuple = ('apple', 'banana', 'orange')
print(f"List size: {sys.getsizeof(fruit_list)} bytes")  # Output: List size: 88 bytes
print(f"Tuple size: {sys.getsizeof(fruit_tuple)} bytes")  # Output: Tuple size: 72 bytes

# Creation comparison
list_creation = ['a', 'b', 'c'] * 1000
tuple_creation = ('a', 'b', 'c') * 1000
print(f"Length of list_creation: {len(list_creation)}")  # Output: Length of list_creation: 3000
print(f"Length of tuple_creation: {len(tuple_creation)}")  # Output: Length of tuple_creation: 3000

# Length comparison
print(f"Length of list: {len(['a', 'b', 'c'])}")  # Output: Length of list: 3
print(f"Length of tuple: {len(('a', 'b', 'c'))}")  # Output: Length of tuple: 3

# Membership testing
print(f"'a' in list: {'a' in ['a', 'b', 'c']}")  # Output: 'a' in list: True
print(f"'a' in tuple: {'a' in ('a', 'b', 'c')}")  # Output: 'a' in tuple: True

# Max and min operations
print(f"Max of list: {max([1, 2, 3])}")  # Output: Max of list: 3
print(f"Max of tuple: {max((1, 2, 3))}")  # Output: Max of tuple: 3
print(f"Min of list: {min([1, 2, 3])}")  # Output: Min of list: 1
print(f"Min of tuple: {min((1, 2, 3))}")  # Output: Min of tuple: 1

# Sorting and reversing
print(f"Sorted list: {sorted([3, 1, 2])}")  # Output: Sorted list: [1, 2, 3]
print(f"Sorted tuple: {sorted((3, 1, 2))}")  # Output: Sorted tuple: [1, 2, 3]
print(f"Reversed list: {list(reversed([1, 2, 3]))}")  # Output: Reversed list: [3, 2, 1]
print(f"Reversed tuple: {tuple(reversed((1, 2, 3)))}")  # Output: Reversed tuple: (3, 2, 1)