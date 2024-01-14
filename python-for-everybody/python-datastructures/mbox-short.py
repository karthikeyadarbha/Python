# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 08:10:22 2024

@author: hp
"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
fltval = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        ss = line.strip()
        ns = ss.split()
        count = count + 1
        fltval = fltval + float(ns[1])
avg = fltval/count
print('Average spam confidence:',avg)