#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:48:40 2019

@author: thomassullivan
"""

'''
Takes a string of raw text and filters the text by averaging the ord values of each word.
'''

def ord_average(word):
    '''
    Converts the text into a list separated by a space, then each letter is
    converted into its corresponding ord() value. This function returns the 
    average ord value of a word.
    '''
    ord_list = [ord(i) for i in word]
    ord_average = sum(ord_list)/len(ord_list)
    return ord_average

def get_cleaned_text(text, min_ord_value=95, max_ord_value=125):
    '''
    text is self explanatory, min_ord_value removes the phrases where the average
    This function removes the words where the ord_average is less than 
    '''
    text_list = text.split()
    text_values = text.split()
    text_avg_values = [ord_average(i) for i in text_values]
    #bs = BeautifulSoup(html, 'html.parser')
    
#    new_average = bs.text
#    #new_average = new_average.lower()
#    new_average_list = new_average.split()
#    new_average_values = new_average.split()
#    new_average_values = [ord_average(i) for i in new_average_values]
    
    z = zip(text_list, text_avg_values)
    z1 = list(z)
    z2 = [list(i) for i in z1]
    
    cleaned_list = [i for i in z2 if i[1] >= min_ord_value and i[1] <= max_ord_value]
    cleaned_list_text = [i[0] for i in cleaned_list]
    cleaned_list_string = ' '.join(cleaned_list_text)
    return cleaned_list_string

if __name__ == '__main__':
    text = input('enter text: ')
    result = get_cleaned_text(text, min_ord_value = 95, max_ord_value = 125)
    print(result)
    