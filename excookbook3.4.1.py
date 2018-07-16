#以二进制、8进制、或16进制表示数值
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
#如果不希望出现0b、0o、或者0x的前缀可以使用format函数
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))
#整数是有符号的，如果处理负号的话，输出也会带上一个符号
x = -1234
print(format(x,'b'))
print(format(x,'x'))

#如果要表示一个负数的无符号数值可以使用这种方式实现：
print(format(2 ** 32 + x,'b'))
print(format(2**32 + x,'x'))
#如果要将字符串形式的整数转换成不同的进制，只需要使用int()
print(int('4d2',16))
print(int ('10011010010',2))
