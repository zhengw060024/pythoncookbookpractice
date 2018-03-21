#对一个字典或者对象实例，针对某个特定的字段(比如日期)来分组迭代数据.
#可以使用itertools.groupby()来对数据进行分组
#groupby()需要扫描序列找出相同值，并将其分组,所以需要序列先排序
from operator import itemgetter
from itertools import groupby
rows = [
    {'address':'5412 N CLARK','data':'07/01/2012'},
    {'address':'5148 N CLARK','data':'07/04/2012'},
    {'address':'5800 E 58TH','data':'07/02/2012'},
    {'address':'2122 N CLARK','data':'07/03/2012'},
    {'address':'5645 N RAVENSWOOD','data':'07/02/2012'},
    {'address':'1060 N ADDISON','data':'07/02/2012'},
    {'address':'4801 N BROADWAY','data':'07/01/2012'},
    {'address':'1039 N GRANVILLE','data':'07/04/2012'}
]
rows.sort(key = itemgetter('data'))

for data,items in groupby(rows,key = itemgetter('data')):
    print(data)
    for i in items:
        print(' ',i)
#如果衹是簡單根據日期將數據分組到一起，可以使用multidict
#這種方法要比groupby更快一些
from collections import defaultdict
row_by_data = defaultdict(list)
for item in rows:
    row_by_data[item['data']].append(item)
print(row_by_data['07/01/2012'])