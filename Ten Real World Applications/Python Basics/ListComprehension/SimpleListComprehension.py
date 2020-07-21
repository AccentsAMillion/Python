# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:03:02 2020

@author: Chris
"""

temps = [221, 234, 340, 238 ]

# How to create a new list without creating a for loop
newTemps = [temp / 10 for temp in temps]

print(newTemps)

