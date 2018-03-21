#刪選列表中數據，最簡單的方法是使用列表推導
mylist = [1,4,-5,10,-7,2,3,-1]
temp = [n for n in mylist if n > 0]
print(temp)
temp = [n for n in mylist if n < 0]
print(temp)
#其缺點是如果原始輸入很大，可能會產生一個很大的結果,如果這個是需要考慮的問題，可以使用
#生成器表達式通過迭代的方式來傳聲篩選的結果
pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

#有時候篩選的標準沒法簡單的表示在列表推導公式或者生成器表達式中，可以通過内建的filter()函數處理
#filter 創建的是一個迭代器，如果需要列表形式，就需要在前面加上list
values = ['1','2','-3','-','4','N/A','5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int,values))
print(ivals)

#更多列表表達式和生成器表達式的例子
import math
print([math.sqrt(n) for n in mylist if n > 0])

clip_neg = [n if n > 0 else 0 for n in mylist]
print (clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

addresses = [
    '5412 N CLARK',
    '5418 N CLARK',
    '5800 N 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRAYVILLE'
]
#另一个工具使itertools.compress(),它可接受一个可迭代对象以及一个bool选择器序列作为输入
#输入时，他会给出所有在相应的bool选择器中为True的可迭代对象元素。
counts = [0,3,10,4,1,7,6,1]
from itertools import compress
more5 = [n > 5 for n in counts]

print (more5)
print(list(compress(addresses,more5)))
#方法2
itemResult = (addresses[index]  for index in range(len(counts)) if counts[index] > 5)
print(list(itemResult))
