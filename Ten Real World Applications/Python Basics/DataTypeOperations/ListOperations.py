# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 08:29:19 2020

@author: Chris
"""

# Basic Tempurature lists
tempuratures = [110, 88.7,-50]
tempuratures.append(88.3)
print(tempuratures)
tempuratures.clear()
print(tempuratures)
tempuratures = [110, 88.7,-50, 88.3]
print(tempuratures)
print(tempuratures.index(88.3))
print(tempuratures.index(110))
print(tempuratures.index(-50))
print(tempuratures.index(2))   # ValueError: 2 is not in list won't print anything

# =============================================================================
# 
# dir(list)
# 'append',
#  'clear',
#  'copy',
#  'count',
#  'extend',
#  'index',
#  'insert',
#  'pop',
#  'remove',
#  'reverse',
#  'sort']
# 
# =============================================================================
