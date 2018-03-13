# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 21:08:14 2018

@author: HP
"""

class A:
    com_name = "siva"
#    name
    
    def __init__(self):
        self.name = "bravi"
        self.sal = 123.0
#    @classmethod
    def details(self):
        print(A.com_name)
        name = "ravi"
        sal = 125.0
        print(name,sal)
        
a = A()
a.details()
