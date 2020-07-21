# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:28:51 2020

@author: Chris
"""

# Creating a for loop to round the data to nearest number

temperatures = [9.1, 8.8 , 7.6]
for temp in temperatures:
    print(round(temp))

# Rounding temperatures without using a loop
print(round(temperatures[0]))
print(round(temperatures[1]))
print(round(temperatures[2]))