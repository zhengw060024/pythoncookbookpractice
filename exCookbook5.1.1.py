#读写文本文件
#rt模式会将字符串末尾的/r/n转成/n
with open('exCookbook5.1.1.py','rt',encoding = 'UTF8') as f:
    data = f.read()
    print(data)
print('line Reading!!!')
with open('exCookbook5.1.1.py','rt',encoding = 'UTF8') as f:
    for line in f:
        print(line,end='')