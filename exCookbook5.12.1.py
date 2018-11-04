#检测文件是否存在
#可以使用os.path
import os
print(os.path.exists('/etc/pathwd'))
print(os.path.exists('./exCookbook5.9.1.py'))
print(os.path.isfile('./exCookbook5.9.1.py'))
print(os.path.isdir('./exCookbook5.9.1.py'))
print('testxxxx is a folder. %r' % os.path.isdir('./testxxxx'))
print('testxxxx is a folder. {}'.format(os.path.isdir('./testxxxx')))
print(os.path.getsize('./exCookbook5.9.1.py'))
time1 = os.path.getatime('./exCookbook5.9.1.py')
print(time1)
import time
print(time.ctime(time1))
#os.path对文件检测非常有效，但是有时需要注意权限问题
