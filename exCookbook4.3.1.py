#使用生成器创建新的迭代模式
def frange(start ,stop ,increment):
    x = start
    while x < stop:
        yield x
        x += increment
for item in frange(0,10,0.5):
    print(item,end = ' ')
#函数中只要出现yield语句就会将其转变成一个生成器，但是与普通函数不同，生成器只会在响应迭代操作时
#才会运行。
def countdown(n):
    print('Starting to count from',n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')
print('')
print('common func calling')
c = countdown(3)
print('iterate calling')
next(c)
