import math
data={}
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
class IdNode(Node):
    def __init__(self, id):
        self.id=id
    def evaluate(self):
        return data[self.id]

class IfNode(Node):
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def execute(self):
        # print(self.v1.evaluate())
        # print(self.v1.evaluate())
        if self.v1.evaluate() is True:
            # print(self.v1.evaluate())
            self.v2.execute()
            # print(0)
        # return  0
class ifelseNode(Node):
    def __init__(self,v1,v2,v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3
    def execute(self):
        # print(self.v3.sl)
        if self.v1.evaluate() is True:
            self.v2.execute()
        else:
            self.v3.execute()
class whileNode(Node):
    def __init__(self, v1,v2):
        self.v1=v1
        self.v2=v2
    def execute(self):
        # print(self.v2.sl)
        while self.v1.evaluate() is True:
            # print(data)
            # print(self.v2.sl[0].v2.evaluate())
            self.v2.execute()
            # print(data)
        # return 0
        # print(data)
        # self.v2.execute()
        # print(data)
        # print(self.v2.sl)
        # while self.v1.evaluate() is True:
        #     # print(data)
        #     return self.v2.execute()
        # print(data)
        # return self.v2
class assignNode(Node):
    def __init__(self, v1,v2):
        self.v1=v1
        self.v2=v2
    def execute(self):
        if type(self.v2) is ListNode:
            data[self.v1]=self.v2.evaluate()
        elif type(self.v2) is BopNode:
            data[self.v1]=self.v2.evaluate()
        elif type(self.v2) is IdNode:
            data[self.v1]=self.v2.evaluate()
        elif type(self.v2) is ListNode:
            # print(self.v2.evaluate())
            data[self.v1]=self.v2.evaluate()
            # print(data)
        else:
            # print(data)
            data[self.v1]=self.v2.value
        return 0
class assignListNode(Node):
    def __init__(self,v1,v2,v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3
    def execute(self):
        # print(self.v1+" "+self.v2+" "+self.v3)
        if type(self.v2) is IdNode:
            # print(1)
            self.v2=self.v2.evaluate()
        else:
            self.v2=self.v2.value
        # print(self.v3)
        if type(self.v3) is ListNode:
            data[self.v1][self.v2]=self.v3.evaluate()
        elif type(self.v3) is BopNode:
            data[self.v1][self.v2]=self.v3.evaluate()
        elif type(self.v3) is IdNode:
            data[self.v1][self.v2]=self.v3.evaluate()
        else:
            data[self.v1][self.v2]=self.v3.value
class assignlis(Node):
    def __init__(self, v1,v2):
        self.v1=v1
        self.v2=v2
    def evaluate(self):
        return data[self.v1][self.v2.evaluate()]
        
class StringNode(Node):
    def __init__(self,v):
        self.value=v[1:-1]
    def evaluate(self):
        return self.value

class BooleanNode(Node):
    def __init__(self,v):
        self.value=v
    def evaluate(self):
        return self.value
class ListNode(Node):
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def evaluate(self):
        if self.v2 is None:
            # print(1)
            return self.v1
        # print(self.v1.evaluate()[self.v2.evaluate()])
        if type(self.v1) is not list:
            self.v1=self.v1.evaluate()
            if type(self.v1[self.v2.value]) is BlockNode:
                return self.v1[self.v2.value].sl
            elif type(self.v1) is str:
                return self.v1[self.v2.value]
            elif type(self.v1) is IdNode:
                return data[self.v1.evaluate()][self.v2.evaluate()]
            else:
                return self.v1[self.v2.value]
        elif type(self.v1[self.v2.value]) is BlockNode:
            return self.v1[self.v2.value].sl
        elif self.v2 is None:
            return self.v1
        else:
            return self.v1[self.v2.value]

class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        # print(data)
        # print(data[self.v1.id])
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
            # print(1)
            print("SEMANTIC ERROR")
class BoNode(Node):
    def __init__(self, op, v):
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
        # print(data)
        if type(self.value) is str:
            print(data[self.value])
        else:
            self.value = self.value.evaluate()
            if type(self.value) is str:
                print(self.value)
            elif self.value is None:
                pass
            else:
                print(self.value)


class BlockNode(Node):
    def __init__(self, s):
        self.sl = [s]

    def execute(self):
        # print(self.sl)
        for statement in self.sl:
            # print(statement)
            # if statement is None:
            #     pass
            # else:
            statement.execute()
            # print(1)
# reserved={
#     # 'if' : 'IF'#,
#     # 'else' : 'ELSE',
#     # 'while' : 'WHILE'
# }
tokens = [
    'LBRACE', 'RBRACE',
    'PRINT','LPAREN', 'RPAREN', 'SEMI','IF','ELSE','WHILE',
    'NUMBER','IN','COMMA','LRACE','RRACE','ASSIGN','ID',
    'PLUS','MINUS','TIMES','DIVIDE','STRING','POWER','MODULUS','FLOOR','LESS','GREAT','LESSEQU','GREATEQU','EQU','NOTEQU','AND','OR','NOT','BOOLEAN'
    ]#+list(reserved.values())

# Tokens
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_LRACE=r'\['
t_RRACE=r'\]'
# t_PRINT    = 'print'
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
# t_AND=r'and'
# t_OR=r'or'
# t_NOT=r'not'
# t_IN=r'in'
t_COMMA=r','
t_ASSIGN=r'='
t_ID='[a-zA-Z_][a-zA-Z_0-9]*'

def t_PRINT(t):
    r'print'
    # print(t)
    return t
def t_IF(t):
    r'if'
    return t
def t_ELSE(t):
    r'else'
    return t
def t_WHILE(t):
    r'while'
    return t
def t_AND(t):
    r'and'
    return t
def t_OR(t):
    r'or'
    return t
def t_NOT(t):
    r'not'
    return t
def t_IN(t):
    r'in'
    return t

def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_STRING(t):
    r'\"([^\\"]|(\\.))*\"|\'([^\\\']|(\\.))*\''
    t.value=StringNode(t.value)
    return t
def t_BOOLEAN(t):
    r'True|False'
    if t.value=='True':
        t.value=True
    else:
        t.value=False
    t.value=BooleanNode(t.value)
    return t
# def t_ID(t):
#     r'\b(?:(?!if|else|while|print|and|or|not|in)[a-zA-Z_][a-zA-Z_0-9]*)\b'
#     # print(t)
#     # print(t.value)
#     # print(data)
#     # t.type=reserved.get(t.value,'ID')
#     # print(1)
#     if t.value == 'print':
#         # print(1)
#         pass
#     else:
#         # print(2)
#         return t

def t_error(t):
    # print(t)
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

def p_block(t):
    """
    block : LBRACE inblock RBRACE
    """
    # print(t[2].sl)
    t[0] = t[2]
def p_blockempty(t):
    '''
    block : LBRACE RBRACE
    '''
    t[0]=t[0]

def p_inblock(t):
    """
    inblock : smt inblock
    """
    t[0] = t[2]
    t[0].sl.insert(0,t[1])

def p_smt(t):
    """
    smt : print_smt
    """
    t[0] = t[1]
def p_print_smt(t):
    """
    print_smt : PRINT LPAREN expression RPAREN SEMI
    """
    # print(t[3])
    t[0] = PrintNode(t[3])
def p_smt_if(t):
    '''
    smt : IF LPAREN expression RPAREN LBRACE inblock RBRACE
    '''
    # print(t[3].evaluate())
    t[0]=IfNode(t[3],t[6])
    # t[0]=t[0].execute()
# def p_smt_2(t):
#     '''
#     smt : ID ASSIGN expression
#     '''

def p_smt_ifelse(t):
    '''
    smt : IF LPAREN expression RPAREN LBRACE inblock RBRACE ELSE LBRACE inblock RBRACE
    '''
    t[0]=ifelseNode(t[3],t[6],t[10])
    # t[0]=t[0].execute()
    # print(t[0].v2.execute())
def p_smt_while(t):
    '''
    smt : WHILE LPAREN expression RPAREN LBRACE inblock RBRACE
    '''
    # print(t[3].op)
    t[0]=whileNode(t[3],t[6])
    # print(t[6].sl)
    # print()
    # t[0]=t[0].execute()
def p_smt_1(t):
    '''
    smt : ID ASSIGN expression SEMI
    '''
    # print(t[3])
    # print(t[3].evaluate())
    t[0]=assignNode(t[1],t[3])
def p_smt_2(t):
    '''
    smt : ID LRACE factor RRACE ASSIGN expression SEMI
    '''
    t[0]=assignListNode(t[1],t[3],t[6])
# def p_expression_id(t):
#     '''expression : ID LRACE factor RRACE'''
#     # print(t[3].evaluate())
#     t[0]=assignlis(t[1],t[3])
    # print(t[0])
# def p_expression_doubleid(t):
#     '''expression : expression LRACE factor RRACE'''
#     t[0]=t[1]

def p_expression_index(t):
    '''expression : LRACE inblock RRACE LRACE factor RRACE'''
    t[0]=ListNode(t[2].sl,t[5])

def p_expression_index1(t):
    '''expression : LRACE inblock RRACE'''
    # print(t[2].sl)
    t[0]=ListNode(t[2].sl,None)
    # t[0].sl.insert(0,t[0])
    # print(t[0])

def p_inblock_list(t):
    '''inblock : expression COMMA inblock'''
    t[0] = t[3]
    # print(t[1].evaluate())
    if type(t[1]) is ListNode:
        t[0].sl.insert(0,t[1].evaluate())
    else:
        t[0].sl.insert(0,t[1].value)
    # print(t[0].sl)
def p_expression_index2(t):
    '''expression : expression LRACE factor RRACE'''
    # print(t[1])
    t[0]=ListNode(t[1],t[3])
def p_inblock_list4(t):
    '''inblock : LRACE inblock RRACE'''
    t[0] = BlockNode(t[2])
# def p_expression_list1(t):
#     '''expression : LRACE inblock RRACE'''
#     t[0] = BlockNode(t[2])




def p_inblock2(t):
    """
    inblock : smt
    """
    t[0] = BlockNode(t[1])

def p_inblock3(t):
    """
    inblock : expression
    """
    # print(t[1])
    if type(t[1]) is ListNode:
        # print(t[1].evaluate())
        t[0]=BlockNode(t[1].evaluate())
    else:
        t[0] = BlockNode(t[1].value)
    # print(t[0].sl)
# def p_inblock4(t):
#     '''
#     inblock : LRACE inblock RRACE
#     '''
#     t[0]=BlockNode(t[1])

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
def p_facor_id(t):
    'factor : ID'
    t[0]=IdNode(t[1])
def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]
def p_error(t):
    # print(t)
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
    code=''
    for i in range (0,len(message)):
        code+=message[i]
    # print(code)
    try:
        result=yacc.parse(code)
        result.execute()
    except Exception:
        pass
main();
