# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:28:31 2018

@author: HP
"""

#[1,2,6,-8,-7,17,-1,3,0]
#def maxsum(array):
#    if len(array)==0:
#        print('too small')
#    maxsum = currsum = array[0]
#    for i in array[1:]:
#        currsum = max(currsum + i,i)
#        maxsum = max(currsum,maxsum)
#    return maxsum
#print(maxsum([1,2,6,-8,-7,17,-1,3,0]))


def maxsum(array):
    array.sort(reverse=True)
    maxi = array[0]+array[1]
    return print(maxi)
maxsum([1, 2, 6, -8, -7, 17, -1, 3, 0])