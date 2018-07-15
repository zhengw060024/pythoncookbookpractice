#在字节串上执行文本操作
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello',b'Hello Cruel'))
#几乎所有能在字符串上执行的操作同样可以在字节串上进行，但是对于访问字节的
#字节流和str流類型是不同的。
a  = 'Hello World'
print(a[0])
b = b'Hello World'
print(b[0])
#在字节流上不能进行格式化操作