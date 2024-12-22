import time
import random

def exponential_backoff_with_loop(max_retries, max_delay=32):
    # Initial delay before the first retry attempt
    delay = 1
    
    # Loop for the number of retries
    for attempt in range(1, max_retries + 1):
        try:
            # Simulate an operation (e.g., network request)
            print(f"Attempt {attempt}: Trying operation...")
            if random.choice([True, False]):  # Simulate a 50% chance of failure
                raise Exception("Operation failed")  # Simulate failure
            print("Operation succeeded!")
            return  # Exit if the operation is successful
        except Exception as e:
            print(f"Attempt {attempt}: {e}")
            if attempt < max_retries:
                # Exponential backoff with randomization
                sleep_time = min(delay * 2 ** (attempt - 1), max_delay)  # Exponential backoff with cap
                sleep_time += random.uniform(0, 1)  # Add randomization to avoid sync retries
                print(f"Retrying in {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)  # Wait before the next retry
            else:
                print("Max retries reached. Giving up.")
                return  # Stop retrying after max retries

# Example usage
exponential_backoff_with_loop(5)
