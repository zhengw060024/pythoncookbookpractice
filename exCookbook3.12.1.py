#时间换算
from datetime import timedelta
a = timedelta(days=2,hours = 6)
b = timedelta(hours=4.5)
c = a + b
print('a is {} b is {} c is {}'.format(a,b,c))
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

#如果需要表示特定的日期和时间，可以创建datetime实例并使用标准的数学运算符来操纵他们
from datetime import datetime
a = datetime(2012,9,23)
print(a + timedelta(days = 10))
b = datetime(2012,12,21)
d = b -a 
print(d.days)
print(d)
now = datetime.today()
print(now)
print(now + timedelta(minutes = 10))

#当执行计算的时候，datatime模块是可以正确处理闰年的
a = datetime(2012,3,1)
b = datetime(2012,2,28)
print (a - b)
print((a - b).days)
c = datetime(2013,3,1)
d = datetime(2013,2, 28)
print((c - d).days)
#datetime可以满足大部分需求，如果需要处理更加复杂的日期问题，处理时区，模糊时间范围
#计算节日日期等，可以使用dateutil
#dateutil可以处理datetime在处理关于月份问题上能填补一些datetime留下的空缺
from dateutil.relativedelta import relativedelta
a = datetime(2012,9,23)
#这里注意是months
print((a + relativedelta(months = +1)))
b = datetime(2012,12,21)
d = relativedelta(b,a)
print(d)

