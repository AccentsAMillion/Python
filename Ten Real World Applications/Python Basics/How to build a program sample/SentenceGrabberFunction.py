# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 02:39:14 2020

@author: Chris
"""
text = ""

def sentence_grabber(phrase):
    interrogatives = ("how", "what", "when", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    
print(sentence_grabber("it's a good day here, the weather is so nice"))
print(sentence_grabber("how is the weather were you are at"))
print(sentence_grabber("there is only some clouds here, but overall nice day"))