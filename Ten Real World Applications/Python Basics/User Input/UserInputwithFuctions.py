# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:28:25 2020

@author: Chris
"""
# Creating a function for weather and using a variable to request user input

def weather_condition(temperature):
    if temperature < 20:
       return "Freezing"
    elif temperature > 20 and temperature < 50:
        return "Warm"
    else:
        return "Hot"

# To get user input to see the int and not str must add float function or int functions 
userInput = float(input("What is the current temperature" ))
print(weather_condition(userInput))
    