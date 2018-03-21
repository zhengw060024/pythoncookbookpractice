#让字典保持有序
#可以使用collection模块中的OrderedDict类。
#此类在对字典做迭代是，会严格按照元素初始添加顺序进行
from collections import OrderedDict
import json
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key,d[key])
print(json.dumps(d))
#OrderedDist 内部维护一个双向链表，第一个新加入的元素会被放置在链表末尾。
#OrderedDist 是普通链表的两倍大小，所以使用时需要注意。
