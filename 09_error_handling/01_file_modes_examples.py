"""
This script demonstrates the various file modes in Python:
'r', 'w', 'a', 'r+', 'w+', 'a+'.
Each mode is implemented with reusable functions and examples.
"""

# Function to write data to a file (overwrites existing content)
def write_file(file_name, content):
    """
    Writes data to a file. Overwrites existing content.
    
    Args:
        file_name (str): The name of the file to write to.
        content (str): The content to write.
    """
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"Written to {file_name}: {content}")


# Function to append data to a file
def append_file(file_name, content):
    """
    Appends data to a file. Preserves existing content.
    
    Args:
        file_name (str): The name of the file to append to.
        content (str): The content to append.
    """
    with open(file_name, 'a') as file:
        file.write(content + '\n')
    print(f"Appended to {file_name}: {content}")


# Function to read data from a file
def read_file(file_name):
    """
    Reads and returns the content of a file.
    
    Args:
        file_name (str): The name of the file to read from.
    
    Returns:
        str: The content of the file.
    """
    with open(file_name, 'r') as file:
        content = file.read()
    print(f"Read from {file_name}:\n{content}")
    return content


# Function to read and write to a file (r+ mode)
def read_write_file(file_name, content_to_add):
    """
    Reads the file content and appends new content to it.
    
    Args:
        file_name (str): The name of the file to read and write.
        content_to_add (str): The content to append.
    """
    with open(file_name, 'r+') as file:
        content = file.read()
        print(f"Initial content of {file_name}:\n{content}")
        file.write(content_to_add + '\n')
        print(f"Appended to {file_name}: {content_to_add}")


# Function to write and read a file (w+ mode)
def write_read_file(file_name, content_to_write):
    """
    Writes new content to a file and then reads it back.
    
    Args:
        file_name (str): The name of the file to write and read.
        content_to_write (str): The content to write.
    """
    with open(file_name, 'w+') as file:
        file.write(content_to_write + '\n')
        file.seek(0)  # Move to the beginning of the file
        content = file.read()
    print(f"Content of {file_name} after writing:\n{content}")


# Function to append and read a file (a+ mode)
def append_read_file(file_name, content_to_append):
    """
    Appends content to a file and then reads the entire file content.
    
    Args:
        file_name (str): The name of the file to append and read.
        content_to_append (str): The content to append.
    """
    with open(file_name, 'a+') as file:
        file.write(content_to_append + '\n')
        file.seek(0)  # Move to the beginning of the file
        content = file.read()
    print(f"Content of {file_name} after appending:\n{content}")


# Main function demonstrating all file modes
if __name__ == "__main__":
    file_name = 'example_file.txt'

    print("\n--- Example 1: Write Mode ('w') ---")
    write_file(file_name, "This is a fresh start.")

    print("\n--- Example 2: Append Mode ('a') ---")
    append_file(file_name, "Appending this line.")

    print("\n--- Example 3: Read Mode ('r') ---")
    read_file(file_name)

    print("\n--- Example 4: Read and Write Mode ('r+') ---")
    read_write_file(file_name, "Adding more content via r+.")

    print("\n--- Example 5: Write and Read Mode ('w+') ---")
    write_read_file(file_name, "Overwriting with w+ mode.")

    print("\n--- Example 6: Append and Read Mode ('a+') ---")
    append_read_file(file_name, "Adding final content via a+.")
