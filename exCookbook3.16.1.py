#处理涉及到时区的日期问题
from datetime import datetime
import pytz
from pytz import timezone
d = datetime(2013,12,21,9,30,0)
print(d)
central = timezone('US/Central')
loc_d = central.localize(d) 
print(loc_d)
#通常用来处理本地时间的方法时将所有的日期都转换为UTC时间，然后处理
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)