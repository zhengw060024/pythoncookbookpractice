#实现优先级队列
import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
#python
class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name) 
q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
#使用元祖(priority, index,item)来表示元素是因为item是无法比较的，而对于相同的元素
#如果不附加index参数也是无法比较的。
#测试格式化输出字符串
strTemp = 'Item({!r})'.format('fdsafdsaf')
print(strTemp)
