# -*- coding: utf-8 -*-
"""
Created on Sun May  3 05:16:28 2020

@author: Chris
"""

def sentence_grabber(phrase):
    interrogatives = ("how", "what", "when", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    userInput = input("Say something clever: ")
    if userInput == "\end":
        break
    else:
        results.append(userInput)
        
print(" ".join(results))