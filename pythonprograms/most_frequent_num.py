# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 12:18:50 2018

@author: HP
"""
#this program is to find the most frequent element from a list
def most_freq(a):
    a = sorted(a)
#    b = set(a)
    max_count = 0
    max_item = None
    count = {}
    for i in a:
        if i not in count:
            count[i]=1
        else :
            count[i]+=1
#            return count
        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    print(count)
    return max_item
    
print(most_freq([1,1,1,2,3,3,4,4,4,4]))