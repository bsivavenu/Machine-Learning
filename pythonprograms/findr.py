# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 22:19:27 2018

@author: HP
"""

def findr(a1,a2):
    a1.sort()
    a2.sort()
    for i,j in zip(a1,a2):
        if i != j :
            return i
#        else :
    return  a1[i]
#            return a1[i]
x = findr([1,2,3,4,6,7,5],[6,3,1,4,2,5])
print(x)

import collections
def findr(array1, array2):
    d = collections.defaultdict(int)
    for num in array2:
        d[num] += 1
    for num in array1:
        if d[num]==0:
            return num
        else:
            d[num] -= 1
x = findr([1, 2, 3, 4, 6, 7, 5], [6, 3, 1, 4, 2, 5])
print(x)
def findr(a1,a2):
    x = list(set(a1)-set(a2))
    return print(x)
findr([1, 2, 3, 4, 6, 7, 5,99], [6, 3, 1, 4, 2, 5])