filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = ['Makefile','foo.c','bar,py','spam.c','spam.h']
#endswith 传入元组，备注一定是元组
filterNames = [name for name in filenames if name.endswith(('.c','.h'))]
print(filterNames)