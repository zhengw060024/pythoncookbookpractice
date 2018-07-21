#在不同的迭代器中迭代
from itertools import chain
a = [1,2,3,4]
b = ['x','y','z']
for x in chain(a,b):
    print(x)
#使用这种方法可以减少独立的循环数目