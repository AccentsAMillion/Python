# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:03:39 2020

@author: Chris
"""
import numpy

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
a = max(numpy.absolute(student_grades))
print(student_grades.count(10.0))
print(student_grades.count(9.1))
print(a)
