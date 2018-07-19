#手动访问迭代器元素
#处理某个可迭代对象中的元素但是基于某种原因不能也不想使用for循环
def openFileTest(strFilePath):
    with open(strFilePath,encoding='UTF8') as f:
        try:
            while True:
                line = next(f)
                print(line,end='')
                #print('ssssss')
            pass
        except StopIteration as identifier:
            pass
#openFileTest('exCookbook3.16.1.py')
#如果是手动使用next()，可以命令其返回一个结束值
def openFileTest2(strFilePath):
    with open(strFilePath,encoding = "UTF8") as f:
        while True:
            line = next(f,None)
            if(line is None):
                break
            else:
                print(line,end='')
openFileTest2('exCookbook3.16.1.py')
items = [1,2,4,5]
print('')
it = iter(items)
for item in it :
    print(item)