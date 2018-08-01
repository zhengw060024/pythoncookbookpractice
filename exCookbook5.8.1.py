#对固定大小的记录进行迭代
#可以使用iter()和functools.partial()来完成这个技巧
from functools import partial
RECORD_SIZE = 32
with open('exCookbook5.8.1.py','rb') as f:
    records = iter(partial(f.read,RECORD_SIZE),b'')
    for r in records:
        print(r)
#如果给迭代器传递一个可调用对象以及一个哨兵值，那么它将创建一个迭代器。
#得到的迭代器会重复调用用户提供的可迭代对象，直到返回值为哨兵值为止。