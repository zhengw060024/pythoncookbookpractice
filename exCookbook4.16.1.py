#使用迭代器取代while循环
#下面的代码可以使用iter来代替
CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        print(data)
#这样的代码可以使用iter()来代替
def readerNoWhile(s):
    for chunk in iter(lambda : s.recv(CHUNKSIZE),b''):
        print(chunk)

#内建函数iter(),它除了可以接收生成器和可迭代对象之外，还可以选择性的
#接受一个无参可调用对象以及一个哨兵值作为输入，当以这种方式使用时，iter()
#会创建一个迭代器，重复调用可调用对象，直到返回哨兵值为止。