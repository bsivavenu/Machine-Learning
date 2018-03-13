# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:06:31 2018

@author: HP
"""

def max_list(a):
    maxi = 0
    for i in a:
        if i>maxi:
            maxi = i
    return maxi
print(max_list([1,32,2]))