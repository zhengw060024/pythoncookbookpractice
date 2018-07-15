#对数值进行取整，将一个浮点数取整到固定的小数位
#使用round，该round会四舍五入
print(round(1.23,1))
print(round(1.27,1))
print(round(-1.27,1))
print(round(1.2324235,3))
#传入的round可以是负数，这样会相应的取整到十位，百位，千位
a = 166453543
print(round(a,-1))
print(round(a,-2))
print(round(a,-3))
#如果只是将数值按照固定位数输出，只要在格式化正定所需要的精度就可以了
x = 1.23456
print(format(x,'0.2f'))
print('{:0.2f}'.format(x))
print(format(x,'0.3f'))
print('value is {:0.3f}'.format(x))
#不要使用round来修正浮点数精度问题，如果需要使用decimal模块