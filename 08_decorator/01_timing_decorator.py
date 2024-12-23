# Problem 1: Timing Function Execution
# File: timing_decorator.py

import time
from functools import wraps

def timing_decorator(func):
    """
    A decorator that measures the time a function takes to execute.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function(n):
    """
    Simulates a slow function by sleeping for `n` seconds.
    """
    time.sleep(n)
    return f"Finished sleeping for {n} seconds"

if __name__ == "__main__":
    print(slow_function(2))  # Example: Measuring execution time
    print(slow_function(3))  # Example: Measuring execution time