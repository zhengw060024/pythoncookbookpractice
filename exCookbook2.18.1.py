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
