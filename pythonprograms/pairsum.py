# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 09:13:55 2018

@author: HP
"""

#def pairsum(array,num): #[1,2,3,2](4)
#    if len(array) < 2:
#        return "too small"
#    seen = set()
#    output = set()
#    for i in array:
#        target = num - i
#        if target not in seen:
#           seen.add(i)
#        else :
#            output.add((min(i,target),max(i,target)))
#    print('\n'.join(map(str,list(output))))
#pairsum([1,2,3,2,5,0,4],5)        
#            
def pairsum(array,num): #[1,2,3,2](4)
    if len(array) == 0:
        return print("invalid array")
    if len(array) == 1:
        if array[0]==num:
            return print((array[0],0))
        else:
            return print("no combination")
        
    seen = set()
    output = set()
    for i in array:
        target = num - i
        if target not in seen:
           seen.add(i)
        else :
            output.add((min(i,target),max(i,target)))
    print('\n'.join(map(str,list(output))))
pairsum([4,2,8,-3,1,0,-2,9,-4,0,3,5],5)        
            