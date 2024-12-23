# Problem 2: Debugging Function Calls
# File: debug_decorator.py

from functools import wraps

def debug_decorator(func):
    """
    A decorator that prints the function name and the values of its arguments 
    every time the function is called.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = ", ".join(map(str, args))  # Convert positional arguments to string
        kwargs_list = ", ".join(f"{k}={v}" for k, v in kwargs.items())  # Convert keyword arguments to string
        print(f"Calling {func.__name__} with arguments: {args_list} {kwargs_list}")
        return func(*args, **kwargs)  # Execute the function
    return wrapper

@debug_decorator
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

@debug_decorator
def greet(name, greeting ="Hello"):
    """
    Returns a greeting message for the given name.
    """
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    print(add(5, 7))  # Example: Debugging a simple addition
    print(greet("janima"))  # Example: Debugging a greeting function
    print(greet("sharma", greeting =" Hi hello"))  # Example: Debugging with a keyword argument