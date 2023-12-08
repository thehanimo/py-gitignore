import sys, os


gitignore_Paths = []
all_Paths = []
all_Files = []
matches = []


root = "C:/Users/Anil/OneDrive/Desktop/Gitignore_Test" #Root directory
f = open(root + "/.gitignore", "r") #Gitignore file

for count, line in enumerate(f):
        pass
count = count + 1 #Gets the number of lines in the Gitignore file

i = 0 #Count for lines
f = open(root + "/.gitignore", "r")
for x in f: #Cycles through each line
    i=i+1
    if i==count:
        gitignore_Paths.append(x) #Adds the last file name to the list
        #print(x)
    else:
        gitignore_Paths.append(x[:-1]) #Removes the newline and adds the file name to the list
        #print(x)
		

for path, subdirs, files in os.walk(root): #Grabs every file path and name from the directory
    for name in files:
        #print(path + "/" + name)
        all_Paths.append(path + "/" + name)
        all_Files.append(name)
		

for i in range(len(all_Paths)): #Fixes the issue with a subdirectory adding a slash as well as changed the direction of the slash for consistency
    all_Paths[i] = all_Paths[i].replace("\\","/")
	
	
for i in range(len(all_Files)): #Finds the matches
    if all_Files[i] in gitignore_Paths:
        matches.append(all_Paths[i])
		

matches