#定义带有额外状态的生成器函数
from collections import deque
class linehistory:
    def __init__(self,lines,histlen= 3):
        self.lines = lines
        self.history = deque(maxlen = histlen)
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append([lineno,line])
            yield line
    def clear(self):
        self.history.clear()

with open('exCookbook3.15.1.py',encoding = 'UTF8') as f:
    lines = linehistory(f)
    for line in lines:
        if 'parse_ymd' in line:
            print('get one item!')
            for lineno,hline in lines.history:
                print('{}:{}'.format(lineno,hline),end='')

#如果生成器函数需要以不寻常的方式同程序中其他部分交互，使用类来定义最好。
#注意在非for循环中使用这样的生成器类需要额外的调用一次iter获取迭代器
