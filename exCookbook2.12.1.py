#文本过滤
import unicodedata
import sys
s = 'python\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t'):' ',
    ord('\f'):' ',
    ord('\r'):' '
}
a = s.translate(remap)
print(a)
#对于Unicode字符可以先做一个映射表，然后，根据映射表去修改
digitMap = {
    c:ord('0') + unicodedata.digit(chr(c)) 
    for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == 'Nd'
}
print(len(digitMap))
x = '\u0661\u0662\u0663'
print(x)
print(x.translate(digitMap))
#对于简单替换操作，str.replace 是最快的方式
def clean_space(s):
    s = s.replace('\r','')
    s = s.replace('\t',' ')
    s = s.replace('\f',' ')
    return s
print(clean_space(s))
