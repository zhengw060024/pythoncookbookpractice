#以不区分大小写的方式对文本做查找和替换
#需要使用re模块并且对各种操作都要加上re.IGNORECASE标记
import re
text = 'UPPER PYTHON, lower python, Mixex Python'
print(re.findall('python',text,flags=re.IGNORECASE))
print(re.sub('python','snake',text,flags=re.IGNORECASE))

#如果要将带替换的文本与匹配的文本大小写相符需要使用一个支撑函数
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
text2 = 'UPPER PYTHON, lower python, Mixex PYthon'
print(re.sub('python',matchcase('snake'),text2,flags=re.IGNORECASE))


