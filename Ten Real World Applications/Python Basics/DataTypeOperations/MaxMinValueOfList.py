# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 08:29:19 2020

@author: Chris
"""

#imported the function numpy
import numpy

# Printing Max Value found in the array
num = [5,6,50,13,-60, 100, 2000, 140, 70]
maxValue = max(numpy.absolute(num))
print(maxValue)

# Prints the minimum value of the array
num = [5,6,50,13,-60, 100, 2000, 140, 70]
minValue = min(numpy.absolute(num))
print(minValue)

