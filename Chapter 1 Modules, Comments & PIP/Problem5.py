# Label the program written in problem 4 with comments.

import os

# Select the directory whose content you want to list down in the terminal
directory_path = '/Your/directory/path'

# Use the os module to list the directory content
contents = os.listdir(directory_path)

# Print the contents of this directory
for item in contents: 
    print(item)