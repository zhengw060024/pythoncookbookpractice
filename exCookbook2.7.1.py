#最短正则匹配表达式
import re
#.在正则表达式中用来匹配任意字符，但是.不能匹配换行符
#贪心匹配
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
#最小匹配
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
