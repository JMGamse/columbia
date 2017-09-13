# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:36:39 2017

@author: pathouli
"""

#!/usr/bin/python                                                               
import sys
freq = {}   # frequency of words in text                                        
for line in sys.stdin:
    for word in line.split():
        if word in freq:
            freq[word] = 1 + freq[word]
        else:
            freq[word] = 1
print freq
