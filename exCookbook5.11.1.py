#处理路径,处理路径名来找出基文件名，目录名，绝对路径等相关信息
import os
path = '/Users/beazley/Data/data.csv'
print(os.path.basename(path));
print(os.path.dirname(path));
print(os.path.join('tmp','data',os.path.basename(path))) 
path = '~/Data/data.csv'
print(os.path.expanduser(path))
print(os.path.splitext(path))