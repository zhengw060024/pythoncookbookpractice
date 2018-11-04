#对二进制文件做内存映射
import os
import mmap
def memory_map(filename, access = mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access = access)

size = 10000
with open('dataTest5101','wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('dataTest5101')
print(len(m))
print(m[0:10])
print(m[0])
m[0:11] = b'Hello World'
m.close()
with open('dataTest5101','rb') as f:
    print(f.read(11))
with memory_map('dataTest5101') as m2:
    print(len(m2))
    print(m2[0:10])
print(m2.closed)

#对于某个文件进行内存映射并不会导致整个文件读到内存中，
#多个Python解释器对同一个文件做了内存映射，得到的mmap对象可以在解释器之间交换数据