# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:13:25 2020

@author: Chris
"""
# how to define an indefinite fuctional arguments
# keyword arguments require 1 asterisk example (*args)
def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4))
print(mean(3, 5, 2, 3, 5, 6, 12, 35, 33))