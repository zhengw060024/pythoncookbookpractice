# 下面这个书上的例子有问题，运行出来出错，有空再看看lex 和 yacc
# https://blog.csdn.net/chosen0ne/article/details/8077880
# from ply.lex import lex
# from ply.yacc import yacc
# tokens = ('NUM','PLUS','MINUS','TIMES','DIVIDE','LPAREN','RPAREN')
# t_ignore = ' \t\n'
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'

# def t_NUM(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

# def t_error(t):
#     print('Bad character:{!r}'.format(t.value[0]))
#     t.skip(1)
# lexer = lex()
# def p_expr(p):
#     '''
#     expr : expr PLUS term
#     | expr MINUS term
#     '''
#     if p[2] == '+':
#         p[0] = p[1] + p[3]
#     elif p[2] == '-':
#         p[0] = p[1] - p[3]
# def p_expr_term(p):
#     '''
#     expr : term
#     '''
#     p[0] = p[1]
# def p_term(p):
#     '''
#     expr : expr TIMES term
#     | expr DIVIDE term
#     '''
#     if p[2] == '*':
#         p[0] = p[1] * p[3]
#     elif p[2] == '/':
#         p[0] = p[1] / p[3]
# def p_term_factor(p):
#     '''
#     term:factor
#     '''
#     p[0] = p[1]
# def p_factor(p):
#     '''
#     factor:NUM
#     '''
#     p[0] = p[1]
# def p_factor_group(p):
#     '''
#     factor: LPAREN expr RPAREN
#     '''
#     p[0] = p[2]
# def p_error(p):
#     print('Syntax error')

# parser = yacc()
# print(parser.parse('2 + 3'))
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------
import sys
if sys.version_info[0] >= 3:
    raw_input = input
 
tokens = (
    'NAME','NUMBER',
    )
 
literals = ['=','+','-','*','/', '(',')']
 
# Tokens
 
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
 
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
 
t_ignore = " \t"
 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()
 
# Parsing rules
 
precedence = (
    ('left','+','-'),
    ('left','*','/'),
    ('right','UMINUS'),
    )
 
# dictionary of names
names = { }
 
def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]
 
def p_statement_expr(p):
    'statement : expression'
    print(p[1])
 
def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
 
def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]
 
def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]
 
def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]
 
def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0
 
def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")
 
import ply.yacc as yacc
yacc.yacc()
 
while 1:
    try:
        s = raw_input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)
