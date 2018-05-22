#文本模式的匹配和查找
text = 'yeah, but no, but yeath, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))
text1 = '11/27/2016'
text2 = 'Nov 27,2016'
import re
if(re.match(r'\d+/\d+/\d+',text1)):
    print('yes')
else:
    print('no')

if(re.match(r'\d+/\d+/\d+',text2)):
    print('yes')
else:
    print('no')  

#如果要匹配多次可以先将正则表达式预编译
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')

#match()总是尝试在字符串的开头找到匹配项。如果想针对整个文本搜索出所有的匹配项
#就应该使用findall()方法。
text = 'Today is 5/22/2018. PyCon starts 3/13/2013.'
print(datepat.findall(text))

#可以使用捕获组的方式来将某个部分提取出来
datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat2.match('5/22/2018')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month,data,year = m.groups()

for month,day,year in datepat2.findall(text):
    print('{}-{}-{}'.format(year,month,day))
#如果想要精确匹配请确保在模式中包含一个结束标记($)