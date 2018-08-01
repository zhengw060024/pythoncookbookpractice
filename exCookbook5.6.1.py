#在字符串上执行I/O操作
#将文本或者二进制字符串写入类似于文件的对象上。
import io
s = io.StringIO()
s.write('Hello world!')
#将输出流重新定向到文件中
print('This is test',file = s)
print(s.getvalue())
s = io.StringIO('Hello \nWorld\n')
print(s.read(4))
print(s.read())
#如果需要操作二进制文件，请使用io.BytesIO
#使用这种方式可以模拟文件，但是没有真正的文件描述符，所以是没法
#用在文件、管道、或套接字代码环境中的。


