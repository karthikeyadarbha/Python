# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 07:59:43 2024

@author: hp
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for word in fh:
    ly = word.rstrip()
    print(ly.upper())

