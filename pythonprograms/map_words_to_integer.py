# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:31:33 2018

@author: HP
"""

#def map_words_to_integer(a):
#    length_words = [len(w) for w in a ]
#    return length_words
#print(map_words_to_integer(['siva','satya','durga']))

def longest_word(a):
#    length_words = [len(w) for w in a ]
#    return max(length_words)
#print(longest_word(['siva','satya','durga tech']))
    for i in a:
        print(i,len(i))
        
print(longest_word(['siva','satya','durga tech']))