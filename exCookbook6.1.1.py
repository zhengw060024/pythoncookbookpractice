#读写csv数据
#可以使用csv库来处理
import csv
with open('users.csv') as f:
    f_csv = csv.reader(f)
    head = next(f_csv)
    for row in f_csv:
        #返回的是一个数组
        print(row)
# 使用命名元组
from collections import namedtuple
with open('users.csv') as f:
    f_csv = csv.reader(f)
    head = next(f_csv)
    print(head)
    Row = namedtuple('Row',head)
    for r in f_csv:
        row = Row(*r) #这里使用*表示按照元素序列顺序传递参数
        print('{} :{} ,{} :{}'.format(head[0],row.userID,head[3],row.Occupation) )
#还有一种方式是将数据读取成字典序列：
#比如
with open('users.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row)
#写入cvs需要创建一个cvs写入对象
with open('users.csv') as f:
    f_csv = csv.reader(f)
    head = next(f_csv)
    with open('userwrite.csv','w') as f2:
        f_csvw = csv.writer(f2)
        f_csvw.writerow(head)
        f_csvw.writerows(f_csv)

#如果是字典序列可以使用DictWriter方法，要注意先先写入head
#如果标题行有非法字符，使用命名元组需要替换特殊字符
import re
with open('users2.csv') as f:
    f_csv = csv.reader(f)
    heads = [re.sub('[^a-zA-Z]','_',h) for h in next(f_csv)]
    print(heads)