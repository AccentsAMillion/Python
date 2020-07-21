# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 07:04:30 2020

@author: Chris
"""

# Creating a List of Students using an array  variable = []
student_grades =[97, 88.5, 100, 48.2, 92.3]

# Takes the total sub function of student_grades and gives it to the variable mySum
mySum = sum(student_grades)
# Uses the length functions to get the total length of student_grades
length = len(student_grades)
# Devides the variable length w/ the variable mySum and prints out the total mean value
mean = mySum / length
print(mean)


