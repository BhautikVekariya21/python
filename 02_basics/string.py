# String examples and methods demonstration

# Basic string creation
my_string = "Hello, Python Programming!"
print("Original string:", my_string)

# String length
print("\nString length:", len(my_string))

# String methods
print("\nString Methods:")
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())
print("Title case:", my_string.title())
print("Capitalize:", my_string.capitalize())
print("Count 'o':", my_string.count('o'))
print("Find 'Python':", my_string.find('Python'))
print("Replace 'Python' with 'ruby':", my_string.replace('Python', 'ruby'))
print("Split string:", my_string.split())
print("Is alphanumeric?", my_string.isalnum())
print("Is alphabetic?", my_string.isalpha())
print("Is digit?", my_string.isdigit())
print("Is lowercase?", my_string.islower())
print("Is uppercase?", my_string.isupper())
print("Strip whitespace:", "  hello  ".strip())

# String slicing
print("\nString Slicing:")
print("First 5 characters:", my_string[0:5])
print("Last 5 characters:", my_string[-5:])
print("Every second character:", my_string[::2])
print("Reverse string:", my_string[::-1])
print("From index 7 to 13:", my_string[7:13])
print("From start to position 10:", my_string[:10])
print("From position 10 to end:", my_string[10:])
print("Middle characters:", my_string[len(my_string)//2-2:len(my_string)//2+2])

# String concatenation
str1 = "Hello"
str2 = "World"
print("\nString Concatenation:")
print("Using + operator:", str1 + " " + str2)
print("Using join method:", " ".join([str1, str2]))
print("Using format method:", "{} {}".format(str1, str2))
print("Using f-string:", f"{str1} {str2}")

# String multiplication
print("\nString Multiplication:")
print("Repeat string 3 times:", str1 * 3)

# Raw string creation
raw_string = r"This is a raw string with \n and \t"
print("\nRaw string:", raw_string)

# String dicing (taking characters at specific intervals)
print("\nString Dicing:")
print("Every third character:", my_string[::3])
print("Every fourth character starting from index 1:", my_string[1::4])
print("Every second character in first half:", my_string[:len(my_string)//2:2])
print("Every third character in last half:", my_string[len(my_string)//2::3])
print("Characters from index 5 to 15 with step 2:", my_string[5:15:2])
print("Reverse string with step 3:", my_string[::-3])

# String formatting
name = "Alice"
age = 25
print("\nString Formatting:")
print("Using % operator:", "Name: %s, Age: %d" % (name, age))
print("Using format() method:", "Name: {}, Age: {}".format(name, age))
print("Using f-string:", f"Name: {name}, Age: {age}")