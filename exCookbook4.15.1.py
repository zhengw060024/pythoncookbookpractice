#合并多个有序序列，再对整个序列进行迭代使用heapq.merge()
#注意，是有序序列
import heapq 
a =[1,3,7,10]
b = [2,5,6,11]
for c in heapq.merge(a,b):
    print(c)