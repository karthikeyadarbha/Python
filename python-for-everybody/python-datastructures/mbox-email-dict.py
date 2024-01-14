# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:32:05 2024

@author: hp
"""

fname = input("Enter file name: ")
fh = open('mshort.txt')
count = 0
#fltval = 0.0
em_dict = dict()
for line in fh:
    emlist = list()
    if line.startswith("From "):
        emlist = line.split()
        old_count = em_dict.get(emlist[1],0)
        newcount = old_count + 1
        em_dict[emlist[1]] = newcount
dval = list(em_dict.values())
dkey = list(em_dict.keys())
print(dkey[dval.index(max(dval))]+' '+str(em_dict[dkey[dval.index(max(dval))]]))