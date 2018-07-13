#字符串合并最快的方法是使用Join
parts = ['Is','Chicago','Not','Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))
#普通的字符串只需要一个+就可以了
a = 'Is Chicago'
b = 'Not Chicago'
print(a + ' ' + b)
#使用+操作符会产生一个新的临时对象，因而使用+操作符去链接大量字符串是非常低效的。
data = ['ACME',50,91.2,'is','what']
#print(type(data[0]))
print(','.join(str(item) for item in data))
print(','.join(str(item) for item in data if type(item) == type('xxx')))
#非必要的字符串连接也要注意下：
a = 'hello'
b = 'world'
c = '!'
print(a+':'+b+':'+c) # 这种写法很糟糕
print(':'.join([a,b,c])) #这种写法不好
print(a,b,c,sep=':')
#在io中的使用
#如果str1和str2 都很小使用第一种方式，反之使用第二种方式
with  open('test2.14.2.1.txt','w') as f:
    str1 = 'E_Attendence'
    str2 = '看看我的考勤'
    f.write(str1 + str2)
with  open('test2.14.2.2.txt','w') as f:
    str1 = 'E_Attendence'
    str2 = '看看我的考勤'
    f.write(str1)
    f.write(str2)
#如果是需要从许多短字符中构建输出，应该考虑构建生成器函数
def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago'

text = ' '.join(sample())
with open('test2.14.2.3.txt','w') as f:
    for item in sample():
        f.write(item)
#当size超过一定限制之后直接将size长度写入文件，反之先在内存中汇总
def combineAi(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size+=len(part)
        if(size > maxsize):
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)
with open('test2.14.2.4.txt','w') as f:
    for part in combineAi(sample(),3):
        f.write(part)