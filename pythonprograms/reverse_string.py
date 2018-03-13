# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:09:54 2018

@author: HP
"""

def reverse(s):
    final_string = s[::-1]
    return final_string
print(reverse('siva'))
print(reverse('william'))
print(reverse('tat'))#this is a palindrome
def palindrome(s):
     s = s.replace(' ','').lower()
     if s[::-1]==s:
         return print(s,': this is a palindrome')
     else:
         print(s,': not a palindrome')
palindrome('tat')
palindrome('good')