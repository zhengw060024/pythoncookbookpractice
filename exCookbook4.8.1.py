#跳过可迭代对象的一部分
#使用itertools模块中的dropwhile
with open('exCookbook4.8.1.py', encoding = 'UTF8') as f:
    for line in f:
        print(line,end= '')
print('')
print('跳过开始的注释')
from itertools import dropwhile
with open('exCookbook4.8.1.py',encoding = 'UTF8') as f:
    for line in dropwhile(lambda line:line.startswith('#'),f):
        print(line,end= '')
#注意这和下面的方式是有区别的。
print('')
print('跳过全部的注释！')
with open('exCookbook4.8.1.py', encoding = 'UTF8') as f:
    #生成一个新的生成器
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line,end= '')
print('')