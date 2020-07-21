# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:28:25 2020

@author: Chris
"""
#To create functions in python it starts with def function():

    # Function to Calculate mean of Dictionary with Conditionals
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
        
    return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7}
print(mean(monday_temperatures))
print(mean(student_grades))

# =============================================================================
# runfile('C:/Users/Chris/Everything Python/Ten Real World Applications/Python Basics/ConditionalIntDictFunction.py', wdir='C:/Users/Chris/Everything Python/Ten Real World Applications/Python Basics')
# print(mean(monday_temperatures))
# 9.266666666666666
# print(mean(student_grades))
# 8.299999999999999

# ======================================================================

# Mor conditional - Conditional blocks will check if true or not
if 3 > 1:
    print("Greater")
else:
    print("Not Greater")

# Equivalence would be
if True:
    print("Greater")
else: 
    print("Not Greater")
    
# =============================================================================
# type(3) == int
# Out[5]: True
# 
# isinstance(3, int)
# Out[6]: True
# =============================================================================
