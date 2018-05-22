#针对任意多的分割符拆分字符串
line = 'asdf fjdk ; afed, asdf ,      foo'
import re
slitResult = re.split(r'\s*[;,\s]\s*',line)
print(slitResult)

