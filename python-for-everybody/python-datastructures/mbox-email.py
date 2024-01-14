# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:54:14 2024

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 08:10:22 2024

@author: hp
"""

fname = input("Enter file name: ")
fh = open('mshort.txt')
count = 0
#fltval = 0.0
em_list = list()
for line in fh:
    em_list = list()
    if line.startswith("From "):
        em_list = line.split()
        print(em_list[1])
        count = count + 1
print('There were '+str(count)+' lines in the file with From as the first word')