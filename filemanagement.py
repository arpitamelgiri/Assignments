# open file in read/text mode (default mode)

fileobj = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test1.txt")
fileobj = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test1.txt", 'r')
fileobj = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test1.txt", 'w')
fileobj = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test1.txt", 'a')

# Close the file
fileobj.close()

# Read file
fileobj = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test2.txt")

# Read whole file
print(fileobj.read())

# File cursor is already at the end of the file so it wont able to read.
print(fileobj.read())

# Bring the file to initial position
fileobj.seek(0)
#print(fileobj.read())


#place file cursor at position 7
fileobj.seek(7)
#print(fileobj.read())


fileobj.seek(0)
print(fileobj.read(22))

# Get the file cursor position
print(fileobj.tell())

# readline() - Reads the line of a file
fileobj.seek(0)

print(fileobj.readline()) # Read first line of a file
print(fileobj.readline()) # Read second line of a file

#readlines() - Read all lines of a file
fileobj.seek(0)
print(fileobj.readlines())

# Read first 5 lines of file using readlines()
fileobj.seek(0)

count = 0
for i in fileobj.readlines():
    if (count < 5):
        print(i)
    else:
        break
    count += 1

# Write file
fileobj1 = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test1.txt", 'w')

# Append content to existing file
fileobj1.write("This is new content appended in the existing file.")
fileobj1.close()

fileobj1 = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test1.txt", 'r')
print(fileobj1.read())

# delete File

import os
os.remove("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test2.txt")

fileobj1 = open("C:/Users/amelgirx/AppData/Local/Programs/Python/Python310/Python stack training/test2.txt", 'r')













