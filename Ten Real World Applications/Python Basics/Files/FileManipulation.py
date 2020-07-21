# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:20:37 2020

@author: Chris
"""

# store file in a variable
# open the file with open("filename")
# if file is in same directory as the working .py directory don't need to specify full path on file
fruitFile = open("fruit.txt")

# Read a File
# Close a File
content = fruitFile.read()
fruitFile.close()

# Read content variable for fruitFile
print(content)

# Better way to handle a file
# No need to use close method with this option implicitly
# "r" parameter is read
with open("fruit.txt", "r" ) as fruitFile:
    content = fruitFile.read()
    
print(content)

# Opening a file in different location thats found in same folder as FileManipulation.py
with open("Alternate File Location/fruit.txt") as fruitFile:
    content = fruitFile.read()
    
print(content)

# Writing text to a file
with open("fruit.txt", "w") as fruitFile:
    appendFruit = fruitFile.write("artichoke\nberry\nmandorin")
    appendFruit = fruitFile.write("\nartichoke\nberry\nmandorin")

# Appending text to a file
with open("fruit.txt", "a+") as fruitFile:
    fruitFile.write("\nartichoke\nmandorin\ncherry\napple\ngrape\n")
    fruitFile.seek(0)
    content = fruitFile.read()
    
print(content)
