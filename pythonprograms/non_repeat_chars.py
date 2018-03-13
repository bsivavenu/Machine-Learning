# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:37:14 2018

@author: HP
"""
#this is to find unique aka non repeatable charecters in a string
def non_repeat(s):
    s = s.replace('  ','').lower()
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c]+=1
        else:
            char_count[c]=1
    for c  in s:   
        if char_count[c]==1:
            return c
    return None
print(non_repeat('hHiaA'))