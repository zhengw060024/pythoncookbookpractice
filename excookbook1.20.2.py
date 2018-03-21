#将多个映射合并为单个映射
a = {'x':1,'z':3}
b = {'y':2,'z':4}
from collections import ChainMap
c = ChainMap(a,b)
print(c)
print(len(c))
print(list(c.keys()))
print(list(c.values()))
#如果有重复的值，会采用第一个映射中所对应的值。
#修改映射的操作总是会作用在第一个映射结构上
# del c['x']