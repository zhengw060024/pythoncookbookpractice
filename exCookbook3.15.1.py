#将字符串转为日期
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
z  = datetime.now()
diff = z - y
print(y)
print(diff)
nice_z = datetime.strftime(z,'%A %B %d, %Y')
print(nice_z)
#strptime比较慢，如果知道日期的格式，可以直接自己编写一个函数
def parse_ymd(s):
    year_s,mon_s,day_s = s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))
print(parse_ymd(text))
