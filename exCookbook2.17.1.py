#在文本中处理HTML和xml实体
s = 'Element are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s,quote=False))
