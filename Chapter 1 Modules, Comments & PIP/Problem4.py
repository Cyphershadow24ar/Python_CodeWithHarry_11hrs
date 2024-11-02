# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

def print_directory_contents(path):
    try:
        for item in os.listdir(path):
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Specify the directory path
directory_path = '/ME'

# Print the contents of the specified directory
print_directory_contents(directory_path)
