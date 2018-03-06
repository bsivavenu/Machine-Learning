# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 17:04:51 2018

@author: HP
"""

from random import randint
def create_array(lenght= 10, maxint= 20):
    new_array = [randint(0,maxint) for _ in range(lenght)]
    return new_array
#print(create_array())

def bubble(array):
    swapped = True
    while swapped:
        swapped = False 
        for i in range(1,len(array)):
            if array[i-1] > array[i]:
                array[i],array[i-1] = array[i-1],array[i] 
                swapped = True
    return array
def  is_sorted(array):
    sorted_array = sorted(array)
    return array == sorted_array

def benchmark(n = [10,100,1000,5000]):
    from time import time
    b0 = [] #bubble
    b1 = [] #builtin
    for length in n:
        a = create_array(length,length)
        
        t0 = time()
        s = sorted(a)
        t1 = time()
        b1.append(t1-t0)
        
        t0 = time()
        s = bubble(a)
        t1 = time()
        b0.append(t1-t0)
    print('n \t builtin\tbubblesort')
    print('......................................')
    for i,cur_n in enumerate(n):
        print("%d \t%0.5f \t%0.5f"%   (cur_n,b1[i],b0[i]))
benchmark()
        
    

#a = create_array()
#print(a)
#a = bubble(a)
#print(a)
#print(is_sorted(a))