# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:39:57 2017

@author: zhxin
"""

def get_word_list_from_txt():
    file = 'hlm2.txt'
    with open(file, encoding='UTF-8') as f:
        l = f.read()
    lines = l.split()   #list of lines
    word_list_primary = []  
    for i in lines:
        for j in i:
            word_list_primary.append(j.strip())
    unicode_list = []
    for i in word_list_primary:
        unicode_list.append(i.encode('unicode-escape'))
    unicode_list_purified = []  #unicode_list elements omitted the punctuations
    for i in unicode_list:
        if i >= b'\\u4e00' and i <= b'\\u9fa5':
            unicode_list_purified.append(i)
    word_list = []  #final output of word list
    for i in unicode_list_purified:
        word_list.append(i.decode('unicode-escape'))
    return word_list
        
