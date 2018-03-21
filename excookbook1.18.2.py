#将名称映射到序列的元素中
#我们的代码通过位置，即索引或下标来访问列表或元组，可以通过nametuple通过名称来访问元素。

from collections import namedtuple
subcriber = namedtuple('Subscribe',['addr','joined'])
sub = subcriber('jonesy@example.com','2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)
#虽然nametuple看起来像某个普通的类实例，但是他的实例与普通的元组是可以互换的，
#而且支持所有的普通元组所支持的操作
print(len(sub))
addr,joined = sub
print(addr)
print(joined)

#下面这样使用records，如果records中序列添加某列，下面的代码就会crash
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

#namedtuple 的一种可能用法是作为字典的替代，后者需要更多的空间来存储，如果要构建涉及字典的大型数据结构
#使用namedtuple会更加高效，与字典不同namedtuple是不可变的。例如：
s = Stock('ACME', 100,123.45)
print(s)
print(s.shares)
#如果需要修改任何属性，可以通过使用namedtuple实例的_replace()方法来实现。该方法会创建一个全新的命名组
s = s._replace(shares= 75)
print(s)
#_replace()方法有一个微妙的用途，他可以作为一种简便的方法填充具有可选或缺失区域的命名元组
Stock = namedtuple('Stock',['name','shares','price','data','time'])
stock_prototype = Stock('',0,0.0,None,None)
def dick_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name':'ACME','shares':'100','price':123.45}
print(dick_to_stock(a))
