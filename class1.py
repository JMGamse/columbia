# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

print "hello"

a = [1,2,3]
a.append(8)


b = list()
b.append(2)
b.append("2")

testDict = {'a': 1, 'b': 2, 'c': 3}

print testDict.keys()

print testDict.values()












for key,value in zip(testDict.keys(),testDict.values()):
    print key, value
    print testDict[key]

mydict = {'adams':14,'washington':15,'hamilton':16}
print mydict.keys()[mydict.values().index(16)]

testDf = pd.read_csv('/media/sf_myStuff/academia/data/dictEx.csv')#,index_col='country_id',names='name')#,header=None)
testDf.index = testDf['country_id']
testDf.drop('country_id',axis=1) 
print testDf.loc[56]
print testDf.iloc[0]




#test = test.to_dict

#test[140]