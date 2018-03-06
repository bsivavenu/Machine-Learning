# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:49:23 2018

@author: HP
"""

import collections
c = collections.Counter("hey how are you")
for i in c:
    print(i,':',c[i],end='\t') 


def fre(word):
    dict = {}
    for n in word:
        b = dict.keys()
        if n in b:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

fre('lord')