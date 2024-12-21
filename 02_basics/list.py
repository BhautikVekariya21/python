
# Creating a list
my_list = [1, 2, 3, 4, 5]

# append() - adds element at end
print("\nAppend example:")
my_list.append(6)
print(my_list)  # [1, 2, 3, 4, 5, 6]

# extend() - adds elements from another list
print("\nExtend example:")
my_list.extend([7, 8, 9])
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert() - adds element at specific index
print("\nInsert example:")
my_list.insert(2, 10)  # insert 10 at index 2
print(my_list)  # [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# remove() - removes first occurrence of value
print("\nRemove example:")
my_list.remove(10)  # removes 10
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# pop() - removes and returns element at index
print("\nPop example:")
popped = my_list.pop(2)  # removes element at index 2
print(f"Popped element: {popped}")
print(my_list)  # [1, 2, 4, 5, 6, 7, 8, 9]

# clear() - removes all elements
print("\nClear example:")
temp_list = [1, 2, 3]
temp_list.clear()
print(temp_list)  # []

# index() - returns index of first occurrence
print("\nIndex example:")
print(my_list.index(4))  # returns index of 4

# count() - counts occurrences of value
print("\nCount example:")
my_list.append(4)
print(f"Number of 4's: {my_list.count(4)}")

# sort() - sorts list in place
print("\nSort example:")
my_list.sort()
print(my_list)  # sorted in ascending order
my_list.sort(reverse=True)
print(my_list)  # sorted in descending order

# reverse() - reverses list in place
print("\nReverse example:")
my_list.reverse()
print(my_list)

# copy() - returns shallow copy of list
print("\nCopy example:")
new_list = my_list.copy()
print(f"Original: {my_list}")
print(f"Copy: {new_list}")

# List slicing
print("\nSlicing examples:")
print(f"First 3 elements: {my_list[:3]}")
print(f"Last 3 elements: {my_list[-3:]}")
print(f"Every second element: {my_list[::2]}")

# List comprehension
print("\nList comprehension example:")
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# len() - returns length of list
print("\nLength example:")
print(f"Length of list: {len(my_list)}")

# max() and min() - returns maximum and minimum values
print("\nMax and Min example:")
print(f"Maximum value: {max(my_list)}")
print(f"Minimum value: {min(my_list)}")

# sum() - returns sum of all elements
print("\nSum example:")
print(f"Sum of all elements: {sum(my_list)}")
# Calculate squares and cubes using for loop and if-else
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        # Calculate square for even numbers
        square = num ** 2
        print(f"{num} is even - Square is: {square}")
    else:
        # Calculate cube for odd numbers
        cube = num ** 3
        print(f"{num} is odd - Cube is: {cube}")
# Simple for loop to traverse list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# Using enumerate() to get both index and value
for index, value in enumerate(numbers):
    print(f"Index {index}: Value {value}")

# Using range and len to traverse by index
for i in range(len(numbers)):
    print(f"Element at index {i} is {numbers[i]}")

# Traversing list in reverse using reversed()
for num in reversed(numbers):
    print(num)

# Traversing with step size of 2
for num in numbers[::2]:
    print(num)

# Creating a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing and modifying nested elements
print("\nOriginal nested list:")
print(nested_list)

# Append to inner list
nested_list[0].append(10)
print("\nAfter appending 10 to first inner list:")
print(nested_list)

# Extend inner list
nested_list[1].extend([11, 12])
print("\nAfter extending second inner list:")
print(nested_list)

# Insert into inner list
nested_list[2].insert(1, 13)
print("\nAfter inserting 13 into third inner list:")
print(nested_list)

# Remove from inner list
nested_list[0].remove(10)
print("\nAfter removing 10 from first inner list:")
print(nested_list)

# Pop from inner list
popped = nested_list[1].pop()
print(f"\nPopped element from second inner list: {popped}")
print(nested_list)

# Sort inner list
nested_list[2].sort(reverse=True)
print("\nAfter sorting third inner list in descending order:")
print(nested_list)

# List comprehension with nested list
squares = [[x**2 for x in inner] for inner in nested_list]
print("\nSquares of all elements using nested list comprehension:")
print(squares)

# Flatten nested list using list comprehension
flattened = [item for sublist in nested_list for item in sublist]
print("\nFlattened list:")
print(flattened)