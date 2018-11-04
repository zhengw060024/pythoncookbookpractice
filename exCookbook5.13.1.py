#获取目录内容的列表
#获取文件系统中某个目录下所包含的文件列表
import os
names = os.listdir('./')
for item in names :
    print(item)
namesDir = (name for name in os.listdir('./') if os.path.isdir(os.path.join('./',name)))
for item in namesDir:
    print('fold is {}'.format(item))
pyfiles = [name for name in os.listdir('./') if name.endswith('.py')]
for item in pyfiles:
    print(item)
#文件名匹配，可以使用glob或者fnmatch模块
import glob
pyfiles = glob.glob('./*.py')
for item in pyfiles:
    print('id {}'.format(item))

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('./') if fnmatch(name,'*.py')]

for item in pyfiles:
    print('id2 {}'.format(item))

file_metadata = [(name,os.stat(name)) for name in pyfiles]
for name,meta in file_metadata:
    print(name,meta.st_size,meta.st_mtime)