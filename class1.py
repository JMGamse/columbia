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

testDf = pd.read_csv('/media/sf_myStuff/academia/data/NVDA.csv',index_col='Date')#,names='name')#,header=None)
ret = testDf.Close.pct_change()
ret.mean()

testDf = testDf.drop('Volume',axis=1) 

print testDf.loc['1999-01-26']['Close']

example = pd.DataFrame(testDf['Close'])
example = example.append(133,ignore_index=True)

test = pd.DataFrame(index=None,columns=['a','b','c'])
#test = test.append({'Ticker':'NVDA','Open': 176,'Close': 200},ignore_index=True)
#test = test.append({'Ticker':'NVDA','Open': 176,'Close': 200},ignore_index=True)

for i in range(0,100):
    test = test.append({'Ticker':'NVDA','Open': int(i),'Close': int(i+12)},ignore_index=True)

test.index = test['Close']
testDf.to_csv('/media/sf_myStuff/academia/data/test.csv')#,names='name')#,header=None)






















#test = test.to_dict

#test[140]