# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:34:25 2024

@author: hp
"""

import regex as re
ftext = open("regex_sum_1957059.txt")
l_sum = 0
for txt in ftext:
    ntext = txt.rstrip()
    t_ex = re.findall('[0-9]+',ntext)
    if len(t_ex) > 0:
        for l in t_ex:
             l_sum = l_sum + int(l)
print(l_sum)