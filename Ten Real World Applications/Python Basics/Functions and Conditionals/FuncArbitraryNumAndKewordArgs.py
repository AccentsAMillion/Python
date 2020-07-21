# -*- coding: utf-8 -*-
"""
Created on Sun May  3 09:13:25 2020

@author: Chris
"""
# how to define an indefinite fuctional arguments
# keyword arguments require 2 asterisk **variableName example (**args)
# Conventional name is kwargs for keyword arguments
def mean(**kwargs):
    return kwargs

# using keyword arguments creates a dictionary
print(mean(a=1, b=3, c=4))
print(mean(a=3, b=5, c=2, d=3, e=5, f=6, g=12, h=35, i=33))