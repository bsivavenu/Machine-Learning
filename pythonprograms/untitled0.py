# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 22:31:23 2018

@author: HP
"""
x = [1,2,3,1,2,3,5]
seen =set()
count = 0
seen =set(x)
print(seen)
for i in x:
    if i in seen:
        count += 1
    else:
        i+=1
    print(x[i],count)