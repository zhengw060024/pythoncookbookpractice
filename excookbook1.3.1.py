

#yield使用
def fab(n):
    nCount ,a,b = 0,0,1
    while(nCount < n):
        yield b
        a,b,nCount = b,a + b,nCount + 1
for nResult in fab(10):
    print(nResult)
#保存最后N个元素
from collections import deque
def search(lines, pattern, history= 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
if __name__ == '__main__':
    with open('test.txt') as f:
        for line, prevlines in search(f,'python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)
#deque在指定maxlen时会创建一个固定长度的队列，当有新纪录加入而队列已经满时会自动移除最老的那条记录
q = deque(maxlen = 3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.append(5)
print(q)
q.pop()
print(q)