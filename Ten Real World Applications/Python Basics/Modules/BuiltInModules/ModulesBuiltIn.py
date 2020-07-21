# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:32:22 2020

@author: Chris
"""
# BuiltIn Modules to utilize in code
import time
import os

while True:
    if os.path.exists("fruit.txt"):
        with open("fruit.txt") as file:
            print (file.read())
    else:
        print("File does not exist.")
        time.sleep(10)
        
