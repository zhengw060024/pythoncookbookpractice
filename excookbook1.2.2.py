#从任意长度的可迭代对象中分解元素
#使用*表达式来解决这个问题
#例如：
def getAvg(inputArray):
    return sum(inputArray)/len(inputArray)
def drop_first_last(grades):
    first,*middle,last = grades
    return getAvg(middle)
gradesArray = [12,45,78,88]
temp = drop_first_last(gradesArray)
print(temp)

user_record = ['Dave', 'dave@example.com', '773-555-1222', '847-555-1212']
name,email,*phone_numbers=user_record
print(name)
print(email)
print(phone_numbers)

*trailing,current = [10,8,7,1,9,5,10,3]
print(trailing)
print(current)

records = [('foo',1, 2),
('bar','hello'),
('foo',3,4)]
def do_foo(x,y):
    print('foo',x,y)
def do_bar(s):
    print('bar',s)
for tag,*args in records:
    if(tag == 'foo'):
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
#处理拆分时:
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(':')
print(uname)
print(homedir)
print(sh)

#有时候想分解某些值，然后丢弃他们
record = ('ACME', 50, 123.45, (12,18,2012))
name,*_,(*_,year) = record
print(name)
print(year)


