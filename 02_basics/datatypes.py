
# Numeric Types
integer_num = 42  # int
float_num = 3.14  # float
complex_num = 2 + 3j  # complex

# String Type
text = "Hello World"  # str
multiline_text = '''This is a
multiline string'''

# Sequence Types 
my_list = [1, 2, 3]  # list
my_tuple = (1, 2, 3)  # tuple
my_range = range(5)  # range

# Mapping Type
my_dict = {"name": "John", "age": 30}  # dict

# Set Types
my_set = {1, 2, 3}  # set
my_frozenset = frozenset([1, 2, 3])  # frozenset

# Boolean Type
is_true = True  # bool
is_false = False

# Binary Types
my_bytes = b"Hello"  # bytes
my_bytearray = bytearray(5)  # bytearray
my_memoryview = memoryview(bytes(5))  # memoryview

# None Type
my_none = None  # NoneType
def get_data_type(value):
    """Returns the data type of the input value"""
    return type(value).__name__

def check_numeric(value):
    """Checks if value is a numeric type (int, float, complex)"""
    return isinstance(value, (int, float, complex))

def check_sequence(value): 
    """Checks if value is a sequence type (list, tuple, range)"""
    return isinstance(value, (list, tuple, range))

def check_mapping(value):
    """Checks if value is a mapping type (dict)"""
    return isinstance(value, dict)

def check_set(value):
    """Checks if value is a set type (set, frozenset)"""
    return isinstance(value, (set, frozenset))

def check_binary(value):
    """Checks if value is a binary type (bytes, bytearray, memoryview)"""
    return isinstance(value, (bytes, bytearray, memoryview))

def is_none(value):
    """Checks if value is None"""
    return value is None

def is_boolean(value):
    """Checks if value is boolean"""
    return isinstance(value, bool)

def is_string(value):
    """Checks if value is string"""
    return isinstance(value, str)

# Testing all data type checking functions with example values

# Numeric Types
print("Testing numeric types:")
print(f"get_data_type(42): {get_data_type(42)}")
print(f"check_numeric(42): {check_numeric(42)}")
print(f"check_numeric(3.14): {check_numeric(3.14)}")
print(f"check_numeric(2+3j): {check_numeric(2+3j)}")

# String Type
print("\nTesting string type:")
print(f"get_data_type('Hello'): {get_data_type('Hello')}")
print(f"is_string('Hello'): {is_string('Hello')}")

# Sequence Types
print("\nTesting sequence types:")
print(f"get_data_type([1,2,3]): {get_data_type([1,2,3])}")
print(f"check_sequence([1,2,3]): {check_sequence([1,2,3])}")
print(f"check_sequence((1,2,3)): {check_sequence((1,2,3))}")
print(f"check_sequence(range(5)): {check_sequence(range(5))}")

# Mapping Type
print("\nTesting mapping type:")
print(f"get_data_type({{'a':1}}): {get_data_type({'a':1})}")
print(f"check_mapping({{'a':1}}): {check_mapping({'a':1})}")

# Set Types
print("\nTesting set types:")
print(f"get_data_type({1,2,3}): {get_data_type({1,2,3})}")
print(f"check_set({1,2,3}): {check_set({1,2,3})}")
print(f"check_set(frozenset([1,2,3])): {check_set(frozenset([1,2,3]))}")

# Boolean Type
print("\nTesting boolean type:")
print(f"get_data_type(True): {get_data_type(True)}")
print(f"is_boolean(True): {is_boolean(True)}")

# Binary Types
print("\nTesting binary types:")
print(f"get_data_type(b'Hello'): {get_data_type(b'Hello')}")
print(f"check_binary(b'Hello'): {check_binary(b'Hello')}")
print(f"check_binary(bytearray(5)): {check_binary(bytearray(5))}")
print(f"check_binary(memoryview(bytes(5))): {check_binary(memoryview(bytes(5)))}")

# None Type
print("\nTesting None type:")
print(f"get_data_type(None): {get_data_type(None)}")
print(f"is_none(None): {is_none(None)}")

def is_boolean(value):
    """Checks if value is boolean"""
    return isinstance(value, bool)

def is_string(value):
    """Checks if value is string"""
    return isinstance(value, str)

def is_boolean(value):
    """Checks if value is boolean"""
    return isinstance(value, bool)

def is_string(value):
    """Checks if value is string"""
    return isinstance(value, str)