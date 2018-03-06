# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:03:57 2018

@author: HP
"""

def compare(a1,a2):
    if len(a1)==len(a2):
        if set(a1)==set(a2):
            return print("they are same")
    else:
        return print("arrays are not same")
a1 = [1,2,3]
a2 = [3,1,2,4]
compare(a1,a2)

def compare(a1,a2):
    if len(a1)==len(a2):
        for i in a1:
            if a1[i] in a2:
                return print("they are same")
    else:
        return print("arrays are not same")
a1 = [1,4,2,3]
a2 = [3,1,2,4]
compare(a1,a2)

