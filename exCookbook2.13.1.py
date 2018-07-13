#python 对齐文本,可以指定填充字符
text = 'hello world'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
#format函数也可以完成任务，使用'<','>'或者'^'字符以及一个期望的宽度
print(text.ljust(20,'-'))
print(text.rjust(20,'+'))
print(text.center(20,'*'))
print('use format')
print(format(text,'>20'))
print(format(text,'<20'))
print(format(text,'^20'))

print(format(text,'->20'))
print(format(text,'+<20'))
print(format(text,'=^20'))
#尽量使用format而不是%来格式化字符串
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))
print(format(x,'<10.2f'))
#在格式化多个值时，可以使用format
print('{:>10s}{:>10s}'.format('hello','world'))
print('{:<10.2f}{:>10.3f}'.format(1.3435,3.46546))
