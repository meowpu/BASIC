#########################################
#TOKENS
#########################################

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN='LPAREN'
TT_RPAREN = 'RPAREN'

class Token:
    def __init__(self,type_,values):
        self.type = type_
        self.value=value

    def __repr__(self):
        if(self.value): return f'{self.type}:{self.value}'
        return f'{self.type}'
    

##################################
#LEXER
##################################

class Lexer:
    def __init__(self,text):
        self.text=text
        self.pos = -1
        self.current_char = None

    def advance(self):
        self.pos+=1
        self.current_char = self.text[pos]
