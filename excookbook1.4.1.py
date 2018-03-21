#找到最大或最小的N个元素
import heapq
nums = [1, 8, 2, 23, 7, -4,18,23,42,37,2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
#heapq可以接受一个参数key
portfolio = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'AAPL', 'shares':50,'price':543.22},
    {'name':'FB', 'shares':200, 'price':21.09},
    {'name':'HPQ','shares':35,'price':31.75},
    {'name':'YHOO','shares':45, 'price':16.35},
    {'name':'ACME', 'shares':75, 'price':115.65}
]
cheap = heapq.nsmallest(3,portfolio,key = lambda s:s['price'])
expensive = heapq.nlargest(3,portfolio,key= lambda s:s['price'])
print('the most three cheapst is %s'%cheap)
print('the most expensive is %s'%expensive)
heap = list(nums)
heapq.heapify(heap)
print(nums)
print(heap)


