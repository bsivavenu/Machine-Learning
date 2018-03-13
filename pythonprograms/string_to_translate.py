# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:06:32 2018

@author: HP
"""

def translate(string_to_translate):
    '''
    Doubles every consonant and adds an o between them
    '''

    final_string = ''

    for char in string_to_translate:
        if char not in ('aeiou'):
            final_string += (char + 'o' + char)
        else:
            final_string += char

    return(final_string)
print(translate('siva'))
