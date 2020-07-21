# -*- coding: utf-8 -*-
"""
Created on Sun May  3 08:57:11 2020

@author: Chris
"""

# Keyword and non-keyword arguments
# Default and non-default parameters

def area(a,b):
    return a * b

# positional and nonkeyword arguments are the same thing the 3 and 7
print(area(3, 7))

#keywordArguments position doesn't matter
print(area(b=7, a=3))

#default arguments
def area(a, b=7):
    return a * b

print(area(a=3))
# or since a = 3 only need to define b and you get same answer
print(area(3))

# and take a=3 and change variable b to a different value
print(area(3, b=5))
