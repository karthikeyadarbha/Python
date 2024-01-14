# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 16:32:40 2024

@author: hp
"""

fname = input("Enter file name: ")
fh = open('mshort.txt')
count = 0
#fltval = 0.0
em_dict = dict()
for line in fh:
    if line.startswith("From "):
        lin = line.rstrip()
        wds = lin.split()
        new_word = wds[5][0:wds[5].find(':')]
        em_dict[new_word] = em_dict.get(new_word,0) + 1
x = sorted(em_dict.items())

for i in range(len(x)):
    print(x[i][0],x[i][1])