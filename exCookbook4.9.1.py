#迭代所有可能的组合或排列
item = ['a','b','c']
from itertools import permutations
for p in permutations(item):
    print(p)
#如果想要得到较短长度的所有全排列，可以提供一个长度参数：
print('较短长度全排列')
for p in permutations(item,2):
    print(p)

#这个全排列不考虑元素是否相同
item = ['a','a','c']
from itertools import permutations
for p in permutations(item):
    print(p)

item = ['a','b','c']
from itertools import combinations
print('print combinations 3')
for c in combinations(item,3):
    print(c)

print('print combinations 2')
for c in combinations(item,2):
    print(c)

print('print combinations 1')
for c in combinations(item,1):
    print(c)



