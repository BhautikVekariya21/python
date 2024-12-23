
# Problem 3: Cache Return Values
# File: cache_decorator.py

from functools import wraps

def cache_decorator(func):
    """
    A decorator that caches the return values of a function, so that when it's 
    called with the same arguments, the cached value is returned instead of 
    re-executing the function.
    """
    cache = {}  # Dictionary to store cached results

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {func.__name__} with arguments: {args}")
            return cache[args]  # Return the cached result
        print(f"Cache miss for {func.__name__} with arguments: {args}")
        result = func(*args)  # Compute the result
        cache[args] = result  # Store the result in the cache
        return result
    return wrapper

@cache_decorator
def factorial(n):
    """
    Computes the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))  # First call (cache miss)
    print(factorial(5))  # Second call (cache hit)
    print(factorial(6))  # New call (cache miss, calculates using cached factorial(5))
