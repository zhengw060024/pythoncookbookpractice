#文本分词
text = 'foo = 23 + 42 * 10'
import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NUM,NAME,PLUS,TIMES,EQ,WS]))
from collections import namedtuple
Token = namedtuple('Token',['type','value'])
def generate_token(pat,text):
    scaner = pat.scanner(text)
    for m in iter(scaner.match,None):
        yield Token(m.lastgroup,m.group())
tokens = (tok for tok in generate_token(master_pat,text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
#在正则表达式中，如果某个模式是另一个较长模式的子串时，就必须确保较长的那个模式先匹配
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
#如上面的正则表达式，其中LE必须放在第一个匹配
mat_pat2 = re.compile('|'.join([LE,LT,EQ]))
#mat_pat2 = re.compile('|'.join([LT,LE,EQ])) #error!!!
#对有可能形成子串的模式要多加小心
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
mat_pat3 = re.compile('|'.join([PRINT,NAME]))
for tok in generate_token(mat_pat3,'printer'):
    print(tok)
