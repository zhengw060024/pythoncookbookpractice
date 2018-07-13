#从字符串中去掉不需要的字符
import re
str = ' hello world \n'
print(str.strip())
print(str.lstrip())
print(str.rstrip())

t = '--------hello==========='
print(t.lstrip('-'))
print(t.strip('-='))
#strip接口对于字符床中间的空格字符不起作用
str = '  hello world \n';
print(str.strip())
#如果要对字符串中间的空格处理需要其他的一些操作
#转义字符是反斜杠 \
str = '    hello      world   \n'
print(str.replace(' ',''))
print(str.strip().replace(' ',''))
print(re.sub(r'\s+',' ',str).strip())
#测试下正则表达式
str = 'E_ATTENDENCE                 查询我的考勤'
splite1 = re.compile(r'([^\s]*)[\s\t]+([^\s].*)')
print(splite1.findall(str))
