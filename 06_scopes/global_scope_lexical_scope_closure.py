# global_scope_lexical_scope_closure.py

# Global Scope, Lexical Scope, and Closure in Python

# 1. **Global Scope**
# - Global scope refers to the area of the program where a variable or function is defined outside of any function or class.
# - Variables and functions defined in the global scope are accessible from anywhere in the code, including within functions, unless shadowed by local variables.

# Example of Global Scope:

x = 10  # Global variable

def print_global():
    # Accessing global variable 'x' inside a function
    print(x)  # Output will be 10

print_global()  # Calling the function to print the global variable


# 2. **Lexical Scope (also known as Static Scope)**
# - Lexical scope refers to the region of a program where a variable can be accessed based on where it was defined.
# - When a function is called, Python will first check if the variable is defined locally (inside the function).
# - If it's not found, Python will look for the variable in the enclosing function (if any), then in the global scope.

# Example of Lexical Scope:

def outer_function():
    # Variable 'x' in outer function's scope
    x = 20
    
    def inner_function():
        # Accessing variable 'x' from the outer function's scope
        print(x)  # Output will be 20
    
    inner_function()

outer_function()  # Calling the outer function to see lexical scope in action


# 3. **Closure**
# - A closure occurs when an inner function has access to variables from its lexical scope, even after the outer function has finished execution.
# - The inner function "remembers" the environment in which it was created, including any variables that were in scope at the time.

# Example of Closure:

def outer_function(outer_variable):
    # 'outer_variable' is in the outer function's scope
    def inner_function(inner_variable):
        # 'inner_variable' is in the inner function's scope
        print(f"Outer variable: {outer_variable}, Inner variable: {inner_variable}")
    
    return inner_function  # Returning the inner function as a closure

# Create a closure
closure = outer_function(10)  # Calling outer_function, passing 10 as argument

# Call the closure with its own argument
closure(20)  # Output will be: Outer variable: 10, Inner variable: 20


# Summary of Key Differences:
# - **Global Scope**: Variables or functions defined outside any function or class. They can be accessed throughout the entire program.
# - **Lexical Scope**: The visibility of variables is determined by the structure of the code (where functions are nested). Inner functions can access variables from their enclosing (outer) functions.
# - **Closure**: A function that retains access to variables from its lexical scope even after the outer function has completed. This allows the inner function to "remember" its environment.


# Practical Use of Closures:
# Closures are useful when you want to create functions that "remember" some data, but you don’t want to expose that data directly to the outside world.
# Closures are often used in callbacks, decorators, and event handlers.

# Example of Closure with Decorators:

def decorator(func):
    def wrapper():
        print("Before function call")
        func()  # Call the original function
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()  # This will print "Before function call", "Hello!", and "After function call"


# End of the script
