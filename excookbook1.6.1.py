#在字典中将键值映射到多个值上
from collections import defaultdict
d = {
    'a':[1,2,3],
    'b':[4,5]
}
e = {
    'a':{1,2,3},
    'b':{4,5}
}
#使用列表还是集合取决于应用意图，如果希望保留元素插入顺序，就用列表，如果希望消除重复，且不在意其
#顺序使用集合
#为了能方便的创建这样的字典，可以使用collections模块中的defaultdict类，它会自动初始化第一个值
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(4)
e['b'].add(5)
print(e)