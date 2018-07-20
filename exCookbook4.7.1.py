#对迭代器进行切片操作
def Count(n):
    while True:
        yield n
        n +=1
c = Count(0)
import itertools
for x in itertools.islice(c,10,20):
    print(x,end = ' ')
#islice()会消耗掉所提供的迭代器中的数据，迭代器中的数据只能访问一次！
