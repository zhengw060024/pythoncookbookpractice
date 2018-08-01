#读写压缩文件
#使用gzip和bz2模块
import gzip
import bz2
def gzipsomefile(strFileName,strType) :
    with open(strFileName,'rt',encoding ='utf-8') as fileInput:
        strfilegzip = strFileName +strType
        if strType == '.gz':
            with gzip.open(strfilegzip,'wt',encoding='utf-8') as filegz:
                filegz.write(fileInput.read())
        elif strType == '.bz2':
            with bz2.open(strfilegzip,'wt',encoding='utf-8') as filegz:
                filegz.write(fileInput.read())
        else:
            print('illegal zip type!')
def showzipfileData(strFileName):
    if strFileName.endswith('.gz'):
        print('this file is a gz file')
        with gzip.open(strFileName,'rt',encoding='UTF-8') as fileread:
            print(fileread.read())
    elif strFileName.endswith('.bz2'):
        print('this file is a bz2 file')
        with bz2.open(strFileName,'rt',encoding='UTF-8') as fileread:
            print(fileread.read())
    else :
        print('this file is not zip file')


gzipsomefile('exCookbook5.7.1.py','.gz')
gzipsomefile('exCookbook5.7.1.py','.bz2')
showzipfileData('exCookbook5.7.1.py.gz')
showzipfileData('exCookbook5.7.1.py.bz2')

#gzip.open()和bz2.open()可以对已经以二进制模式打开的文件进行叠加操作
print('测试叠加操作')
f = open('exCookbook5.7.1.py.gz','rb')
with gzip.open(f,'rt',encoding='utf-8') as g:
    text = g.read()
    print(text)