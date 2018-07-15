from collections import namedtuple
import re
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'
master_pat = re.compile(('|').join([NUM,PLUS,MINUS,TIMES,DIVIDE,LPAREN,RPAREN]))
TOKEN = namedtuple('TOKEN',['type','value'])
def generateTokens(pat,text):
    iterTokens = re.finditer(pat,text)
    for it in iterTokens:
        tok = TOKEN(it.lastgroup,it.group())
        if tok.type != 'WS':
            yield tok
for tok in generateTokens(master_pat,'34 - 45 / (5 *3)'):
    print(tok)
 # exp => term {addop  term}
 # addop => +|-
 # term => factor {mulop factor}
 # mulop=> *|/
 # factor => (exp) | number
 # 方法2：
 # exp => factor{binaryop factor}
 # factor =>(exp)|number

class ExpressionEvaluator():
    def _getOpPriority(self,op):
        if (op.type == 'PLUS' or op.type == 'MINUS'):
            return 1
        elif (op.type == 'TIMES' or op.type == 'DIVIDE'):
            return 2
        else:
            return -1
    def _checkTokenIsOp(self):
        #self._advance()
        newOp = self.nexttok
        if((newOp.type != 'PLUS') and (newOp.type != 'MINUS') 
            and (newOp.type != 'DIVIDE') and (newOp.type != 'TIMES')):
            return False
        return True
    def _expectOpToken(self):
        if not self._checkTokenIsOp():
            raise SyntaxError('Expected ' + self.tok.value)
    def _makeResultBinaryOp(self,leftValue,op,rightValue):
            print('{} {} {} {}'.format(str(leftValue),op.value,str(rightValue),op.type))
            #expr = leftValue
            if(op.type == 'TIMES'):
                #print('{} * {}'.format(leftValue,rightValue))
                leftValue *= rightValue
              
            elif(op.type == 'DIVIDE'):
                #print('{} / {}'.format(leftValue,rightValue))
                leftValue /= rightValue
              
            elif(op.type == 'PLUS'):
                #print('{} + {}'.format(leftValue,rightValue))
                leftValue += rightValue

            elif(op.type == 'MINUS'):
                #print('{} - {}'.format(leftValue,rightValue))
                leftValue -= rightValue
            #print(leftValue)
            return leftValue
    def _binaryGetValue(self,opPriority,leftValue):
        while True:
            if  not self.nexttok or self.nexttok.type == 'RPAREN':
                return leftValue
            else :
                self._expectOpToken()
                newOp = self.nexttok
                newOpPriority = self._getOpPriority(newOp)
                #这里需要注意一下，只有下一个操作符的优先级高于当前opPriority才消费下一个操作符
                if newOpPriority > opPriority:
                    self._advance()
                    leftValue = self._makeResultBinaryOp(leftValue,newOp,self._binaryGetValueOrHigh(newOpPriority))
                else :
                    break
        return leftValue
    def _binaryGetValueOrHigh(self,opPriority):
        expr = self._factor2()
        return self._binaryGetValue(opPriority,expr)
    def term(self):
        exprval = self.factor()
        while(self._accept('TIMES') or self._accept('DIVIDE')):
            op = self.tok.type
            result = self.factor()
            if(op == 'TIMES'):
                exprval *= result
            if(op == 'DIVIDE'):
                exprval /= result
        return exprval
    def _expr2(self):
        return self._binaryGetValueOrHigh(-1)
    def expr(self):
        exprval =self.term()
        while(self._accept('PLUS') or self._accept('MINUS')):
            op = self.tok.type
            result = self.term()
            if op == 'PLUS':
                 exprval += result
            if op == 'MINUS':
                exprval -= result
        return exprval
    def _expect(self,toketype):
        if not self._accept(toketype):
            raise SyntaxError('Expected ' + toketype)
    def factor(self):
        if self._accept('NUM'):
            result = int(self.tok.value)
            return result
        elif self._accept('LPAREN'):
            result = self.expr()
            self._expect('RPAREN')
            return result
        else:
            raise SyntaxError('Expected NUM or LPAREM')     
    def _factor2(self):
        if self._accept('NUM'):
            result = int(self.tok.value)
            return result
        elif self._accept('LPAREN'):
            result = self._expr2()
            self._expect('RPAREN')
            return result
        else:
            raise SyntaxError('Expected NUM or LPAREM')      
    def parse(self,text):
        self.tokens = generateTokens(master_pat,text)
        self.tok = None #最后一个处理的运算符
        self.nexttok = None #下一个要处理的运算符
        self._advance() #加载第一个运算符
        return self.expr()
    def parse2(self,text):
        self.tokens = generateTokens(master_pat,text)
        self.tok = None #最后一个处理的运算符
        self.nexttok = None #下一个要处理的运算符
        self._advance() #加载第一个运算符
        return self._expr2()
    def _advance(self):
        self.tok ,self.nexttok = self.nexttok,next(self.tokens,None)
    def _accept(self,toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

teste = ExpressionEvaluator()
print(teste.parse('38 * (4 - 12) * 5 / 4'))
print(teste.parse2('38 * (4 - 12) * 5 / 4'))
print(teste.parse2('38 * ((4 - 12) * ((5 -2) +3 *5 )* (2-4) / 4)'))
print(teste.parse('38 * ((4 - 12) * ((5 -2) +3 *5 )* (2-4) / 4)'))

#如果要构建解析树可以通过修改ExpressionEvaluator来实现
class ExpressionTreeBuilder(ExpressionEvaluator):
    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval = ('+',exprval,right)
            elif op == 'MINUS':
                exprval = ('-',exprval,right)
        return exprval
    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval = ('*',termval,right)
            elif op == 'DIVIDE':
                termval = ('/',termval,right)
        return termval
    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUM or LPAREM')  
testCase2 = ExpressionTreeBuilder()
print(testCase2.parse('2 + 3'))
print(testCase2.parse('2 + (3 + 4) * 5'))
print(testCase2.parse('2 + 3 * 4'))