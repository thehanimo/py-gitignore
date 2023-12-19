# Run it this way in CLI: python gitignore.py c:/Users/Anil/Downloads/x/Gitignore_Test


import os
import sys

gitignore_Paths = []
all_Paths = []
all_Files = []
matches = []

args = sys.argv

#root = "c:/Users/Anil/Downloads/x/Gitignore_Test"  # Root directory
try:
    root = args[1]
except IndexError:
    print("No argument given.")
    exit(1)

try:
    f = open(root + "/.gitignore", "r")  # Gitignore file
except FileNotFoundError:
    print("Can't find file.")
    exit(1)

count = 0
for count, line in enumerate(f):
    pass
count = count + 1  # Gets the number of lines in the Gitignore file

i = 0  # Count for lines
f = open(root + "/.gitignore", "r")
for x in f:  # Cycles through each line
    i = i + 1
    if i == count:
        gitignore_Paths.append(x)  # Adds the last file name to the list
    else:
        gitignore_Paths.append(
            x[:-1]
        )  # Removes the newline and adds the file name to the list


# Grabs every file path and name from the directory
for path, subdirs, files in os.walk(
    root
):
    for name in files:
        # print(path + "/" + name)
        all_Paths.append(path + "/" + name)
        all_Files.append(name)


# Fixes the issue with a subdirectory adding a slash as well as
# changed the direction of the slash for consistency
for i in range(
    len(all_Paths)
):
    all_Paths[i] = all_Paths[i].replace("\\", "/")


for i in range(len(all_Files)):  # Finds the matches
    if all_Files[i] in gitignore_Paths:
        matches.append(all_Paths[i])


print(matches)
