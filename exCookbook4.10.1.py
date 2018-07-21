#以索引-值对的形势迭代序列,使用enumerate()
from collections import defaultdict
my_list = ['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)
#可以自定义起始索引
for idx ,val in enumerate(my_list,1):
    print(idx,val)

#'fsfsd'.startswith
#这种情况适合追踪文件中的行号。
word_summary = defaultdict(list)
with open ('exCookbook4.10.1.py',encoding = 'UTF8') as f:
    lines = f.readlines()
lines = (line for line in lines if not line.startswith('#'))
for idx ,line in enumerate(lines):
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)
print(word_summary)

#处理元祖序列时，要注意加括号
data = [(1,2),(3,4),(5,6),(7,8)]
#注意括号
for n ,(x,y) in enumerate(data,1):
    print(n,x,y)