#同时对数据做转换和换算
nums = [1,2,3,4,5]
s = sum(x * x for x in nums)
print(s)
import os
foldpath = os.path.dirname(os.path.realpath(__file__)) 
print(foldpath)
files = os.listdir(foldpath)
if any(name.endswith('.py') for name in files) :
    print ("There be python!")
else :
    print('Sorry, no python.')

s = ['ACME',50 , 123.45]
print(','.join(str(x) for x in s))
portfolio = [
    {'name':'GOOG','shares':50},
    {'name':'YHOO', 'shares':75},
    {'name':'AOL','shares':20},
    {'name':'SCOX','shares':65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)

