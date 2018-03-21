p1 = (10,12)
x,y = p1
print(x,y)
data =['ACME', 50, 91.1, (2012,12,21)]
name, shares,price,date = data
print(name)
print(date)
print(name,shares,price,date)
#只要是可迭代的对象都可以通过解包来分解
s = 'Hello'
a,b,c,d,e = s
print(a)
print(b)
print(e)
print(c)
#做分解操作时有时想丢弃某些值，可以选用一个不常用的变量名来作为要丢弃的变量名称
data = ['Mytest2',70, 12.1,(2018,3,13)]
_,shares,price,_ = data
print(shares)
print(price)


