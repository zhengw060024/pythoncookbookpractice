#委托迭代：
#构建了一个自定义容器对象，其内部持有一个可迭代对象，想让新容器支持迭代操作
#解决方法，定义一个__iter__()方法，将迭代请求发送到内部对象上。
class Node(object):
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
if __name__ == '__main__':
    root = Node(0)
    child1  = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)
#可以写一个树的访问demo
