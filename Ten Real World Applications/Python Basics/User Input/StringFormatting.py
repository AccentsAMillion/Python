# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:28:25 2020

@author: Chris
"""

# Taking user input and formatting the string of its value

userInput = input("What is your name? ")
message1 = "Hello %s!" % userInput
message2 = "Hello {}!".format(userInput)
print(message1)
print(message2)


# Screen print
# =============================================================================
# runfile('C:/Users/Chris/Everything Python/Ten Real World Applications/Python Basics/StringFormatting.py', wdir='C:/Users/Chris/Everything Python/Ten Real World Applications/Python Basics')
# 
# What is your name? Chris
# Hello Chris!
# Hello Chris!
# =============================================================================

# String formatting using multiple variables
firstName = input("What is your first name? ")
middleName = input("What is your middle name? ")
lastName = input("What is your last name? ")


message1 = "Hello %s %s %s! " % (firstName,middleName,lastName)
print(message1)
message2 = "Hello {} {} {}, ".format(firstName,middleName,lastName)
print(message2, "Welcome to the wonderful world of python!. This is the place where you will be successful in life as well as become an expert in the field of programming.")
