#找出当月日期的范围
from datetime import datetime ,timedelta,date
import calendar
def get_month_range(start_date= None):
    if start_date is None:
        #start_date = datetime.today().replace(day=1)
        #date接口不会返回时间信息
        start_date = date.today().replace(day=1)
        _,days_in_month = calendar.monthrange(start_date.year,start_date.month)
        end_date = start_date+timedelta(days = days_in_month)
        return (start_date,end_date)
a_day = timedelta(days = 1)
first_day,last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day+=a_day
#打印方式2
first_day,last_day = get_month_range()

def date_range(start,stop,step):
    while start < stop:
        yield start
        start+=step
for date in date_range(first_day,last_day,a_day):
    print(date)
    #pass

for d in date_range(datetime(2012,9,1),datetime(2012,10,1),timedelta(hours=6)):
    #print(d)
    pass