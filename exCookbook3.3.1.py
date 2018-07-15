#对数值做格式化输出使用format
x = 1234.56789
print(format(x,'0.2f'))
#当需要限制数值位数时，数值会根据round()函数规则来进行取整
print(format(x,'>10.1f'))
print(format(x,'<10.1f'))
print(format(x,'^10.1f'))
#千位分割
print(format(x,','))
print(format(x,'0,.1f'))
#如果要采用科学计数法只要将f改成e或者E即可
print(format(x,'e'))
print(format(x,'0.2e'))
#指定宽度和精度格式一般为[<>^]?width[,]?(.digits)?