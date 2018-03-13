# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:20:59 2018

@author: HP
"""

def histogram(list_of_integers):
    '''
    Prints a histogram based on the list of integers
    '''

    for integer in list_of_integers:
        print(integer * '*')
histogram([4,2,3,4,5])