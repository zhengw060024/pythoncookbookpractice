#同时迭代多个序列
#注意打包函数以两个之中的最短的一个为结束
#当其中某个序列没有元素可迭代时就结束
xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99,87]
for x,y in zip(xpts,ypts):
    print(x,y)

a = [1,2,3]
b = ['w','x','y','z']
for i in zip(a,b):
    print(i)
#如果这种行为不是必须的可以使用zip_longest()
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

#zip只是一个迭代器，如果需要将配对保存，请使用list函数
print(zip(a,b))
print(list(zip(a,b)))
