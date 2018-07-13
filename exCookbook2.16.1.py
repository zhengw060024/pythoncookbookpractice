import textwrap
with open('test2.16.1.txt','r') as f:
    s = f.read()
    print(s)
    print(textwrap.fill(s, 70))
    print(textwrap.fill(s,40))
    print(textwrap.fill(s, 40,initial_indent=' '))
    print(textwrap.fill(s,40, subsequent_indent=' '))
