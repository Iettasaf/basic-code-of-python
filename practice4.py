# Directory Listing Example in Python
import os
#specify the directory you want to list
directory_path = '/New folder'

#List all the path and directorices in the specific path
contents = os.listdir(directory_path)
#print each file and directory name
for item in contents:
    print(item)