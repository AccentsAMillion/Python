# -*- coding: utf-8 -*-
"""
Created on Sun May 24 05:39:53 2020

@author: Chris
"""

import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
    else:
        print("file does not exist")
    time.sleep(10)
    
