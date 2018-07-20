#反向迭代：
#使用内建的reverseed()函数实现反向迭代
a = [1,2,3,4]
for  x in reversed(a):
    print(x)
#反向迭代只有在待处理对象有可确定大小，后者对象实现了__reversed__()特殊方法时才有效
with open('exCookbook3.15.1.py',encoding = 'UTF8') as f :
    for line in reversed(list(f)): #将可迭代对象转换为列表或消耗内存，尤其是可迭代对象较大时。
        print(line,end='')
#可以在自定义类上实现__reversed()__方法来实现反向迭代
class Countdown:
    def __init__(self,start):
        self.start = start
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n+=1
CountItems = Countdown(10)
for item in iter(CountItems):
    print (item,end =' ')
print('')
for item in reversed(CountItems):
    print(item,end = ' ')
print('')