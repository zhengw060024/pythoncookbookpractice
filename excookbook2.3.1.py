#利用Shell通配符做字符串匹配
#可以使用fnmatch模块来匹配
#这些函数可以处理非文件名字符串
from fnmatch import fnmatch ,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))

