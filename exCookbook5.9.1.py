#将二进制数据读取到可变缓冲区中使用readinto
import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf
with open('sample591.bin','wb') as f:
    f.write(b'Hello World')
buf = read_into_buffer('sample591.bin')
print(buf)
buf[0:5] = b'hallo'
print(buf)
with open('newsample.bin','wb') as f:
    f.write(buf)
#f.readinto()需要注意的是必须总是要检查他的返回值，即实际读取的字节数。
#如果字节数小于所提供的缓冲区大小，这可能表示数据被截断或遭到破坏。