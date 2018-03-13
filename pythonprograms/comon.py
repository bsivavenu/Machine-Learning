# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:55:51 2018

@author: HP
"""
#This programs is to get the common elements from two arrays
def comn(a1,a2):
    i = 0
    j = 0
    com = []
    while i < len(a1) and j < len(a2):
        a1 = sorted(a1)
        a2 = sorted(a2)
        if a1[i] == a2[j]:
            com.append(a1[i])
            i += 1
            j += 1
        elif a1[i] > a2[j]:
            j += 1
        else :
            i += 1
    return com

s1 = [1,2,4,8,9]
s2 = [1,2,3,8,2]

print(comn([1,3,8,2],[1,2,4,8,9]))  
print(comn(s1,s2))
print(comn([3,8,2,0],[0,4,8,9]))  
