#创建处理数据的管道
#使用生成器函数
import os 
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat,top):
    for path,dirlist,filelist in os.walk(top):
        for name in fnmatch.filter(filelist,filepat):
            yield os.path.join(path,name)

def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename,'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename,'rt')
        else:
            f = open(filename,'rt',encoding = 'UTF8')
            yield f
            f.close()
def gen_concatenate(iterators):
    for it in iterators:
        yield from it
def gen_grep(pattern,lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line

longnames = gen_find('exCookbook*','.')
files = gen_opener(longnames)
lines = gen_concatenate(files)
#括号里的意思表示不区分大小写
pylines = gen_grep('(?i)python',lines)
for line in pylines:
    print(line)