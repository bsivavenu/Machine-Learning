# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:49:55 2018

@author: HP
"""

def palindrome_sentance_recog(a):
    strip_sentance = ("".join(e for e in a if e.isalnum()))
    strip_sentance = strip_sentance.lower()
    if strip_sentance==strip_sentance[::-1]:
        return True
    else:
        return False
print(palindrome_sentance_recog('i  dood i'))