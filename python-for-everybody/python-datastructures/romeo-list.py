# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:10:43 2024

@author: Kartheek
"""
fname = input("Enter file name: ")
fh = open("romeo.txt")
lst = list()
nlst = list()
for line in fh:    
    for l in line.split(): 
        if l not in lst: lst.append(l)
lst.sort()
print(lst)

