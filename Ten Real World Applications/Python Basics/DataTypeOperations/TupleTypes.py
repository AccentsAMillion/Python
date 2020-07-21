# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:57:34 2020

@author: Chris
"""

#Tuple Types consist of () instead of list [] brackets
monday_temperature = (1,4,5)
print(monday_temperature)

# With List Arrays you can add, append, or delete an item from it
monday_temperature2 = [1,4,5]
print(monday_temperature)
monday_temperature2.append(6)
monday_temperature2.append(7)
monday_temperature2.append(8)
monday_temperature2.append(9)
print(monday_temperature2)
monday_temperature2.remove(9)
print(monday_temperature2)
monday_temperature2.remove(5)
print(monday_temperature2)
monday_temperature2.append(5)
monday_temperature2.append(9)


# =============================================================================
# # You cannot add or append to a tuple like you can with a list
# monday_temperature3 = (1,4,5)
# monday_temperature3.append(6,7,8)
# print(monday_temperature3)
# =============================================================================
# 
# monday_temperature3.append(5)
# Traceback (most recent call last):
# 
#   File "<ipython-input-55-dfddca73cb4f>", line 1, in <module>
#     monday_temperature3.append(5)
# 
# AttributeError: 'tuple' object has no attribute 'append'
# # =============================================================================
# =============================================================================
# In [60]: monday_temperature.remove(5)
# Traceback (most recent call last):
# 
#   File "<ipython-input-60-f470a58e4b53>", line 1, in <module>
#     monday_temperature.remove(5)
# 
# AttributeError: 'tuple' object has no attribute 'remove'
# =============================================================================
# =============================================================================
