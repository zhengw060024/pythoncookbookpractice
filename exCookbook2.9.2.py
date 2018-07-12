#将Unicode文本统一表示为规范形式
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print('s1 len is:', len(s1))
print('s2 len is:', len(s2))
import unicodedata
#NFC 表示字符应该是全组成的(即如果可能的话就使用单个代码点)
t1 = unicodedata.normalize('NFC',s1)
t2 = unicodedata.normalize('NFC',s2)
print(t1 == t2)
print(ascii(t1))
#NFD表示应该使用组合字符，每个字符是能拆解的。使用这种方式可以在文本净化中起作用。
t3 = unicodedata.normalize('NFD',s1)
t4 = unicodedata.normalize('NFD',s2)
print(t3 == t4)
print(ascii(t3))
#在文本处理过程中净化文本。
#比如去除文本中所有的音符标记
strTemp = ''.join(c for c in t3 if not unicodedata.combining(c))
print(strTemp)