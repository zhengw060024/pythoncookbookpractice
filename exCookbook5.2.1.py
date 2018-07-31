#将输出重定向到文件中
#书里面是以rt打开的应该是有问题的。
with open('testhelloworld.txt','wt') as f:
    print('Hello world!',file = f)