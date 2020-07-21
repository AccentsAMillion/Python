# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:03:02 2020

@author: Chris
"""

temps = [221, 234, 340, -9999, 238 ]

# for loop conditional
# How to create a new list without creating a for loop
newTemps = [temp / 10 for temp in temps]

print(newTemps)

# if conditional
# Using an If condition to check for a value in temp 
# Since we don't want -9999 it will print other existing values
newTemps = [temp / 10 for temp in temps if temp != -9999]

print(newTemps)

#If-else conditional
newTemps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(newTemps)


