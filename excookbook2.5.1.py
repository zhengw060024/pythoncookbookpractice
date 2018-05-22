#查找和替换文本
#对于简单的文本使用str.replace()即可比如
text = 'yeah,but no ,but yeah, but no, but yeah'

print(text.replace('yeah','yep'))
#针对更加复杂的模式，可以使用re模块中的sub()函数/方法。假设我们想把日期从
#"11/27/2012"改写成"2012-11-27"
text = 'Today is 11/27/2012.Python starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
strTemp = datepat.sub(r'\2-\1-\3',text)
print(strTemp)
#针对更复杂的情况的可以指定一个替换回调函数
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))
print(datepat.sub(change_date,text))
#除了得到替换后的文本外还想知道一共完成了多少次替换，可以使用re.subn()例如：
newtext,n = datepat.subn(r'\3-\1-\2',text)
print('{}  替换次数是{}'.format(newtext,n))
