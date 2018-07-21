#扁平化处理嵌套型序列使用yield from
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。
from collections import Iterable
def flatten(items,ignore_types = (str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else :
            yield x
items = [1,2,[3,4,[5,6],7],8]
for x in flatten(items):
    print(x,end=' ')

#如果想编写生成器将其他的生成器当作子例程调用，yiled from 要比额外的for循环好一些