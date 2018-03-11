# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:49:23 2018

@author: HP
"""

import collections
def find(array):
    c = collections.Counter(array)
    for i in c:
        print(i,':',c[i],end='\t') 

x = [1,1,2,2,3,4,4]
find(x)

def fre(word):
    dict = {}
    for n in word:
        b = dict.keys()
        if n in b:
            dict[n] += 1
        else:
            dict[n] = 1
    return print('\n',dict)

fre([3,4,4,5,6,6,7,7,7,8])
fre('a tree on a flat earth is wrong sentance')
find('a tree on a flat earth is wrong sentance')