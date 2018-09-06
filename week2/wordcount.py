#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# Author: NYC data science <http://nycdatascience.com/>

### part 1
import string
from sys import argv
script, target, number = argv

### part 2
class myfile(file):
    def __init__(self, name, mode):
        file.__init__(self, name, mode)
        
    def __str__(self):
        return "Opening file %s" %self.name
    
    def wordCount(self, punctuation='\n', ignoreCase = True):
        '''
        punctuation: punctuations to remove
    
        returns: a dict contains each word and it's corresponding frequency
        '''
        ## read contents and convert to lower
        try:
            raw_string = self.read()
            if ignoreCase:
                raw_string = raw_string.lower()
        except:
            raise Exception("Can't read file %s"%self.name)
            
        ## reaplce all the punctuations with space
        for i in string.punctuation:
            raw_string = raw_string.replace(i, ' ')
        
        if punctuation != None:
            for i in punctuation:
                raw_string = raw_string.replace(i, ' ')
        
        ## split by space, count each word
        raw_list = raw_string.split(' ')
        result = {}
        for word in raw_list:
            if word in result.keys():
                result[word] += 1
            else:
                result[word] = 1
    
        # remove words with length of 0 and return 
        result = {key:value for (key, value) in result.items() if len(key) != 0}
        return result
    
    def wordCountSort(self, descend = True, punctuation='\n', ignoreCase = True):
        '''
        return the sorted word frequency
        '''
        result = self.wordCount(punctuation, ignoreCase = ignoreCase)
        result = sorted(result.iteritems(), key= lambda x: x[1] , reverse = descend)
        return result
    
    def mostCommonWord(self, num=5, punctuation='\n', descend = True, ignoreCase = True):
        '''
        return the most common words
        '''
        result = self.wordCountSort(punctuation=punctuation, ignoreCase = ignoreCase, descend = descend)
        if num > len(result):
            Warning('There are only %s words'%len(result))
            return result
        else:
            return result[:num]
            
### part 3
f = myfile(target, 'r')
print '%12s:%8s' %('Word', 'Frequency')
print '-----------------------'
for i, j in f.mostCommonWord(int(number)):
	print '%12s:%8s' %(i, j)