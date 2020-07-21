# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:34:11 2020

@author: Chris
"""
monday_temperatures = [97,88.5,100,48.2,98.3]
student_grades ={"Jake": 97, "Michael": 88.5,"Steve": 100, "Frank": 48.2,"Thomas": 92.3}
mySum = sum(student_grades.values())
length =len(student_grades)
mean = mySum / length
print(mean)


# =============================================================================
# dir(dict)
# Out[34]: 
# ['__class__',
#  '__contains__',
#  '__delattr__',
#  '__delitem__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getitem__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__len__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__setitem__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  'clear',
#  'copy',
#  'fromkeys',
#  'get',
#  'items',
#  'keys',
#  'pop',
#  'popitem',
#  'setdefault',
#  'update',
#  'values']
# 
# help(dict.values)
# Help on method_descriptor:
# 
# values(...)
#     D.values() -> an object providing a view on D's values
# 
# 
# student_grades ={"Jake": 97, "Michael": 88.5,"Steve": 100, "Frank": 48.2,"Thomas": 92.3}
# 
# student_grades.values()
# Out[37]: dict_values([97, 88.5, 100, 48.2, 92.3])
# 
# student_grades.keys()
# Out[38]: dict_keys(['Jake', 'Michael', 'Steve', 'Frank', 'Thomas'])
# 
# runfile('C:/Users/Chris/Everything Python/Ten Real World Applications/untitled1.py', wdir='C:/Users/Chris/Everything Python/Ten Real World Applications')
# 85.2
# 
# =============================================================================
