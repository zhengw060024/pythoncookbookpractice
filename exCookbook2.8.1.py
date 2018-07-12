#使用正则表示式进行匹配，希望进行匹配时能够跨越多行
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is 
        a comment*/
        '''
print(comment.findall(text1))
print(comment.findall(text2))
#解決這個問題可以添加對換行符的支持。
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
#(?:.|\n)指定一个非捕获组
print(comment.findall(text1))
print(comment.findall(text2))
#re.compile()函数可以接受一个有用的标记--re.DOTALL.着使得正则表达式中的句点可以匹配所有的字符，包括换行符
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))
#re.compile('')
