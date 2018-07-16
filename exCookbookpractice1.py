#格式化字符串
import re
a = 'Hello'
b = 'Jim'
print(','.join([a,b]))
print('{}, {}'.format(a,b))
print('{name}, {name2}'.format(name=a,name2=b))
#正则表示式
strExpr = '2 * 3 - 5 *   6 + 63 / 3'
print(strExpr)
from collections import namedtuple
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MUL = r'(?P<MUL>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
MINUS = r'(?P<MINUS>-)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'
mat_patten = '|'.join([NUM,PLUS,MUL,DIVIDE,MINUS,WS,LPAREN,RPAREN])
Token = namedtuple('Token',['type','value'])
def generate_tokens(strExpr):
    iters = re.finditer(mat_patten,strExpr)
    for iter in iters:
        if iter.lastgroup != 'WS':
            yield Token(iter.lastgroup,iter.group())
for item in generate_tokens(strExpr):
    print(item)

class ExpressionEvaluator:
    def parse(self,strExpr):
        self.tokens = generate_tokens(strExpr)
        self.tok = None
        self.next_tok = None
        self._advance()

        return self.expr()
    def _advance(self):
        self.tok ,self.next_tok = self.next_tok,next(self.tokens,None)
    def _accept(self,toketype):
        if self.next_tok.type == toketype:
            self._advance()
            return True
        else :
            return False
    def _expect(self,toketype):
        if not self._accept(toketype):
            raise SyntaxError('Expected ' + toketype)
    def factor(self):
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            expr = self.expr()
            self._expect('RPAREN')
            return expr
        else:
            raise SyntaxError('Error input token' + self.tok)
    def expr(self):
        return self.binaryExprOrHigh(-1)
    def  binaryExprOrHigh(self,prePRI):
        factorValue = self.factor()
        return self.binaryExprValue(factorValue,prePRI)
    def _checkIsOp(self,typeToke):
        if typeToke == 'PLUS' or typeToke == 'MUL' or typeToke == 'DIVIDE' or typeToke == 'MINUS':
            return True
        return False
    def _getTokeOpPri(self,typeToke):
        if typeToke == 'PLUS' or typeToke == 'MINUS':
            return 1
        if typeToke == 'MUL' or typeToke == 'DIVIDE':
            return 2
        return -1
    def _makeBinaryOp(self,leftValue,opType,rightValue):
        if opType == 'PLUS':
            leftValue += rightValue
        elif opType == 'MINUS':
            leftValue -= rightValue
        elif opType == 'MUL':
            leftValue *= rightValue
        elif opType == 'DIVIDE':
            leftValue /= rightValue
        return leftValue
    def  binaryExprValue(self,leftValue,prePRI):
        while(True):
            if (not self.next_tok) or self.next_tok.type == 'RPAREN' :
                return leftValue
            if self._checkIsOp(self.next_tok.type):
                newPri= self._getTokeOpPri(self.next_tok.type)
                if newPri > prePRI:
                    self._advance()
                    leftValue = self._makeBinaryOp(leftValue,self.tok.type
                    ,self.binaryExprOrHigh(newPri))
                else :
                    break
            else :
                raise SyntaxError('expect op token,but input token is'+self.next_tok.type)
        return leftValue

                    
TempCase  = ExpressionEvaluator()
print(TempCase.parse('2 *(3 - 5) *  ((4-7) - 6 + 63) / 3'))            


