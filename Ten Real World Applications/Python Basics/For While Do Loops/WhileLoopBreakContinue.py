# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 08:28:51 2020

@author: Chris
"""

# While Looping using user input when entering user name and password
# this is just an example get more complex than this.

# Empty strings
username = "" 
password = ""

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "AccentsAMillion":
        if password != "CoolMan3000":
            continue
        else:
            break
    elif username != "AccentsAMillion":
        if password == "CoolMan3000":
            continue 
    else: 
        print("Incorrect Login and Password")
        break
        
print('Your username is', username, 'and you password is', password)
print('You may now login')



