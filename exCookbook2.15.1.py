#给字符串中的变量名做插值处理
#可以通过字符串的format方法近似模拟出来
s = '{name} has {n} message'
print(s.format(name='Jim',n='32'))
#另一种方式：如果被替代的值确实可以在变量中找到，则可以将format_map()和vars()联合使用
name ='Jack'
n = 35
print(s.format_map(vars()))
#vars有个微妙的特性是其可以作用于类的实例上
class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n
a = Info('Kate',38)
print(s.format_map(vars(a)))
#format()和format_map()的缺点是没法优雅的处理缺少某个值得情况
#出现这种情况一种方法就是单独定义一个带有__missing__()方法字典类
class safesub(dict):
    def __missing__(self,key):
        return '{' +key +'}'
del n
print(s.format_map(safesub(vars())))
#如果常常需要执行这种代码，可以将替换变量的过程隐藏在一个小型的功能函数内
import sys
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Good'
n = 45
print(sub('Hello {name}'))
print(sub('You have {n} message.'))
print(sub('Your name is {name},your favorite color is {color}'))