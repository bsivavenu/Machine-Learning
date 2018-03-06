# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:23:03 2018

@author: HP
"""

#"python is good" ">" "good is python"

#def reverse(s):
#    return " ".join(reversed(s.split()))
#s = "python is good"
#print(reverse(s))

#def revers(s):
#    s = s.split()
#    s.reverse()
#    return s
#s = "hi hello how are you"
#print(revers(s))

def rever(s):
#    s = s.split()
    return " ".join(s.split()[::-1])        
#    return " ".join(s.split())[::-1] even letters will get reversed
s = "hi hello"
print(rever(s))

