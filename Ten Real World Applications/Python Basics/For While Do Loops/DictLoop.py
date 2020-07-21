# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:28:51 2020

@author: Chris
"""

# Looping through a dictionary iterating via items(), keys() values()

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

# Grabs the name and the description of the name
for grades in student_grades.items():
    print(grades)
    
# Grabs the name only no descriptions
for grades in student_grades.keys():
    print(grades)
    
# Grabs only the description not the name
for grades in student_grades.values():
    print(grades)
    
    
# =============================================================================
# runfile('C:/Users/Chris/Everything Python/Ten Real World Applications/Python Basics/For While Do Loops/DictLoop.py', wdir='C:/Users/Chris/Everything Python/Ten Real World Applications/Python Basics/For While Do Loops')
# ('Marry', 9.1)
# ('Sim', 8.8)
# ('John', 7.5)

# Marry
# Sim
# John

# 9.1
# 8.8
# 7.5
# =============================================================================

# You can combine a dictionary for loop with string formatting to create text containing information from the dictionary:

phone_numbers = {"John": "+14455655545", "Marry": "+15658845562"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))