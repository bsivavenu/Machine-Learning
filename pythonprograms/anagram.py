# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 18:31:22 2018

@author: HP
"""

def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()    
    return  sorted(s1) == sorted(s2)
# "god" "dog"
    #impossible ,im possible
print(anagram("god", "dog"))


