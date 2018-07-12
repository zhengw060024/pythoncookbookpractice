#使用正则表达式处理文本需要考虑处理Unicode字符
import re
num = re.compile('\d+')
print(num.match('123'))
print('\u0661\u0662\u0663')
print(num.match('\u0661\u0662\u0663'))
#在python中\d已经可以匹配任意unicode数字字符了


