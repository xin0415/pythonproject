import math
class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0

class NumberNode(Node):
    def __init__(self, v):
        if('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

class StringNode(Node):
    def __init__(self,v):
        self.value=v[1:-1]
    def evaluate(self):
        return self.value

class BooleanNode(Node):
    def __init__(self,v):
        self.value=v
    def evaluate(self):
        # print("in the node"self.value)
        return self.value
class ListNode(Node):
    def __init__(self,v1,v2):
        # print(type(v1))
        self.v1=v1
        self.v2=v2
    def evaluate(self):
        # print(type(self.v1.v1.v1.v1))
        # print(self.v1[self.v2.value])
        # print(self.v1[self.v2])
        # if type(self.v1[self.v2.value]) is BlockNode:
        #     print(self.v1[self.v2.value].sl)
        #     return self.v1[self.v2.value].sl
        # print(self.v2)
        if type(self.v1) is not list:
            self.v1=self.v1.evaluate()
            if type(self.v1[self.v2.value]) is BlockNode:
                return self.v1[self.v2.value].sl
            elif type(self.v1) is str:
                return self.v1[self.v2.value]
            else:
                # print(self.v1[self.v2.value].value)
                return self.v1[self.v2.value].value
        elif type(self.v1[self.v2.value]) is BlockNode:
            return self.v1[self.v2.value].sl
        else:
            return self.v1[self.v2.value].value

class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        try:
            if (self.op == '+'):
                return self.v1.evaluate() + self.v2.evaluate()
            elif (self.op == '-'):
                return self.v1.evaluate() - self.v2.evaluate()
            elif (self.op == '*'):
                return self.v1.evaluate() * self.v2.evaluate()
            elif (self.op == '/'):
                return self.v1.evaluate() / self.v2.evaluate()
            elif(self.op=='**'):
                return math.pow(self.v1.evaluate(),self.v2.evaluate())
            elif(self.op=='%'):
                return self.v1.evaluate() % self.v2.evaluate()
            elif(self.op=='//'):
                return math.floor((self.v1.evaluate()/self.v2.evaluate()))
            elif (self.op=='<'):
                if self.v1.evaluate() < self.v2.evaluate():
                    return True
                else:
                    return False
            elif (self.op=='>'):
                if self.v1.evaluate() > self.v2.evaluate():
                    return True
                else:
                    return False
            elif (self.op=='<='):
                if self.v1.evaluate() <= self.v2.evaluate():
                    return True
                else:
                    return False
            elif (self.op=='>='):
                if self.v1.evaluate() >= self.v2.evaluate():
                    return True
                else:
                    return False
            elif (self.op=='=='):
                if self.v1.evaluate() == self.v2.evaluate():
                    return True
                else:
                    return False
            elif (self.op=='<>'):
                if self.v1.evaluate() != self.v2.evaluate():
                    return True
                else:
                    return False
            elif (self.op=='and'):
                return self.v1.evaluate() and self.v2.evaluate()
            elif (self.op=='or'):
                return self.v1.evaluate() or self.v2.evaluate()
            elif (self.op=='in'):
                return self.v1.evaluate() in self.v2.evaluate()
        except:
                print("SEMANTIC ERROR")
class BoNode(Node):
    def __init__(self, op, v):
        # print( (not v.value))
        self.v = v
        self.op = op

    def evaluate(self):
        if (self.op=='not'):
            if self.v.evaluate() == 'True':
                return False
            elif self.v.evaluate() == 'False':
                return True 
            else:
                return (not self.v.evaluate())


class PrintNode(Node):
    def __init__(self, v):
        self.value = v

    def execute(self):
        self.value = self.value.evaluate()
        if type(self.value) is str:
            print("'"+self.value+"'")
        elif self.value is None:
            pass
        else:
            print(self.value)


class BlockNode(Node):
    def __init__(self, s):
        self.sl = [s]

    def execute(self):
        for statement in self.sl:
            statement.execute()

tokens = (
    'LBRACE', 'RBRACE',
    'PRINT','LPAREN', 'RPAREN', 'SEMI',
    'NUMBER','IN','COMMA',
    'PLUS','MINUS','TIMES','DIVIDE','STRING','POWER','MODULUS','FLOOR','LESS','GREAT','LESSEQU','GREATEQU','EQU','NOTEQU','AND','OR','NOT','BOOLEAN'
    )

# Tokens
t_LBRACE  = r'\['
t_RBRACE  = r'\]'
t_PRINT    = 'print'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMI  = r';'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_POWER=r'\*\*'
t_MODULUS=r'\%'
t_FLOOR=r'//'
t_LESS=r'<'
t_GREAT=r'>'
t_LESSEQU=r'<='
t_GREATEQU=r'>='
t_EQU=r'=='
t_NOTEQU=r'<>'
t_AND=r'and'
t_OR=r'or'
t_NOT=r'not'
t_IN=r'in'
t_COMMA=r','
def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        # print(t.value)
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_STRING(t):
    r'\"([^\\"]|(\\.))*\"|\'([^\\\']|(\\.))*\''
    # r'\'([^\\\']|(\\.))*\''
    # print(t.value)
    t.value=StringNode(t.value)
    # str=t.value[1:-1]
    # newstr="'"+str+"'"
    # print(newstr)

    # newstr=''
    # newstr+=t[1:-1]
    # print(newstr)
    # t.value=newstr
    return t
def t_BOOLEAN(t):
    r'True|False'
    if t.value=='True':
        t.value=True
    else:
        t.value=False
    t.value=BooleanNode(t.value)
    return t

def t_error(t):
    print("SEMANTIC ERROR")
    
# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','LESS','GREAT','LESSEQU','GREATEQU','EQU','NOTEQU'),
    # ('left','AND'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MODULUS','FLOOR','NOT'),
    ('right','POWER'),
    ('right','UMINUS')
    )

def p_smt(t):
    """
    smt : print_smt
    """
    t[0] = t[1]
def p_print_smt(t):
    """
    print_smt : PRINT LPAREN expression RPAREN SEMI
    """
    # print(t[3].v1.v1.v1.v)
    # print(t[3].evaluate())
    t[0] = PrintNode(t[3])

def p_expression_index(t):
    '''expression : LBRACE inblock RBRACE LBRACE factor RBRACE'''
    # print(t[2].execute())
    # print(t[2])
    t[0]=ListNode(t[2].sl,t[5])

def p_inblock_list(t):
    '''inblock : expression COMMA inblock'''
    t[0] = t[3]
    # print(t[1])
    t[0].sl.insert(0,t[1])
    # print(t[0].sl)


def p_expression_index2(t):
    '''expression : expression LBRACE factor RBRACE'''
    t[0]=ListNode(t[1],t[3])
    # print(t[0].v1)
def p_inblock_list4(t):
    '''inblock : LBRACE inblock RBRACE'''
    # t[0]=t[2]
    t[0] = BlockNode(t[2])
# def p_expression_index1(t):
#     '''expression : LBRACE inblock RBRACE'''
#     t[0]=t[2]
#     print(1)
# def p_inblock_index3(t):
#     '''inblock : LBRACE inblock RBRACE'''
#     t[0]=BlockNode(t[2])
# def p_inblock_list2(t):
#     '''inblock : expression COMMA LBRACE inblock RBRACE'''
#     print(t[4])
#     t[0]=t[4]
#     t[0].sl.insert(0,t[1])
    
    # t[0]=t[1]
    # t[0]=t[4]
    # t[0].sl.insert(0,t[1])

def p_inblock(t):
    """
    inblock : smt inblock
    """
    t[0] = t[2]
    t[0].sl.insert(0,t[1])

def p_inblock2(t):
    """
    inblock : expression
    """
    t[0] = BlockNode(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression
                  | expression MODULUS expression
                  | expression FLOOR expression
                  | expression LESS expression
                  | expression GREAT expression
                  | expression LESSEQU expression
                  | expression GREATEQU expression
                  | expression EQU expression
                  | expression NOTEQU expression
                  | expression AND expression
                  | expression OR expression
                  | expression NOT expression
                  | expression IN expression'''

    t[0] = BopNode(t[2], t[1], t[3])
    # print(t[0].evaluate())
def p_expression_boop(t):
    '''expression : NOT expression'''
    t[0] = BoNode(t[1], t[2])

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_factor(t):
    '''expression : factor'''
    t[0] = t[1]

def p_factor_number(t):
    'factor : NUMBER'
    t[0] = t[1]
def p_factor_boolean(t):
    'factor : BOOLEAN'
    t[0] = t[1]

def p_facor_string(t):
    'factor : STRING'
    t[0]=t[1]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_error(t):
    print("SYNTAX ERROR")

import ply.yacc as yacc
yacc.yacc()

import sys
# parser = yacc.yacc()

def main():
    f=open(sys.argv[1],'r')
    message=f.read()
    message=message.split("\n")
    f.close()
    for i in range (0,len(message)):
        code="print("+message[i]+");"
        # print(code)
        try:
            result=yacc.parse(code)
            result.execute()
        except Exception:
            pass
main();
