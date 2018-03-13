# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:41:35 2018

@author: HP
"""

def filter_long_words(list_of_words, length_min):
    '''
    Take a list of words and an int and find all words longer than the int
    '''

    final_word_list = []

    for word in list_of_words:
        if len(word) > length_min:
            final_word_list.append(word)
    return final_word_list
print('\n', filter_long_words(['a', 'bb', 'ccc', 'dddd'], 2))
