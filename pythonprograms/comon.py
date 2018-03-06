# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:55:51 2018

@author: HP
"""

#[1,2,4,5][2,5]
def comn(a1,a2):
    
    i = 0
    j = 0
    com = []
    while i < len(a1) & j < len(a2):
        if a1[i] == a2[j]:
            com.append(a1[i])
            i += 1
            j += 2
        elif a1[i] > a2[j]:
            j += 1
        else :
            i += 1
    return com

a1 = [1,2,3]
a2 = [1,2]

print(comn(a1,a2))  