# 深度优先遍历(Depth-First Traversal)
# 假设给定图G的初态是所有顶点均未曾访问过。
# 在G中任选一顶点v为初始出发点(源点)，
# 则深度优先遍历可定义如下：首先访问出发点v，
# 并将其标记为已访问过；然后依次从v出发搜索v的每个邻接点w。
# 若w未曾访问过，则以w为新的出发点继续进行深度优先遍历，
# 直至图中所有和源点v有路径相通的顶点(亦称为从源点可达的顶点)均已被访问为止。
# 若此时图中仍有未访问的顶点，则另选一个尚未访问的顶点作为新的源点重复上述过程，
# 直至图中所有顶点均已被访问为止。
# 图的深度优先遍历类似于树的前序遍历。
# 采用的搜索方法的特点是尽可能先对纵深方向进行搜索。
# 这种搜索方法称为深度优先搜索(Depth-First Search)。
# 相应地，用此方法遍历图就很自然地称之为图的深度优先遍历。
class Node:
    def __init__(self,value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self,Node):
        self._children.append(Node)
    def __iter__(self):
        yield iter(self._children)
    def depthSeach(self):
        yield self
        for child in self._children:
            yield from child.depthSeach()
        
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    child5 = Node(5)
    child6 = Node(6)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    child1.add_child(child4)
    child2.add_child(child5)
    child2.add_child(child6)
    for item in root.depthSeach():
        print(item)