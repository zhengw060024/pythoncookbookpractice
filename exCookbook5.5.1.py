#对已不存在的文件执行写入操作
#使用x代替w来解决，如果文件存在
# with open('somefilewritex.txt','xt') as f:
#     f.write('Hello world!')

#另一种方法
import os
if not os.path.exists('somefilewritex.txt'):
    with open('somefilewritex.txt','wt') as f:
        f.write('Hello world!')
else:
    print('File already exists!')