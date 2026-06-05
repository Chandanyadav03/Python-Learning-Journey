import os

# select the directory you want to list 
directory_path = '/'

# Use the os module to list the content of the directory
contents = os.listdir(directory_path)

# using for loop to print all the item in the directory
for item in contents:
    print(item)
