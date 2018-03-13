# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:21:20 2018

@author: HP
"""
#this is to find whether the given string have unique charecters or not 
#def unique(s):
#    s = s.replace(' ','')
#    a = set(s)
##    for i in s.split():
#    
#    if len(s) == len(a):
#        return True
#    else:
#        return False
#print(unique("s  i v a"))

def unique(s):
    s = s.replace(' ','')
    charecters = set()
    for letter in s:
        if letter in charecters:
            return False
        else:
            charecters.add(letter)
    return True
print(unique('s i va'))