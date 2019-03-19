from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Begin
        self.lexer.add('BEGIN', r'Begin')
        # Nucleo
        self.lexer.add('NUCLEO', r'Nucleo')
        # Si
        self.lexer.add('SI', r'Si')
        # Imprimir
        self.lexer.add('IMPRIMIR', r'Imprimir')
        # Fin
        self.lexer.add('FIN', r'Fin')
        # Parentesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        # Semi Colon
        self.lexer.add('IDENTIFICADOR', r'[a-z]+[0-9]*')
        # Operators
        self.lexer.add('IGUAL', r'\=')
        # self.lexer.add('COMPARACION', r'\=\='))
        self.lexer.add('MAS', r'\+')
        # Number
        self.lexer.add('INT', r'\d+')
        # String       
        self.lexer.add('STRING', r'".*"')
        # self.lexer.add('STRING', r'^\"[a-z]+\"$')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()

f = open('CodigoMamalon.txt','r')
code = f.read()
f.close()

lexer = Lexer().get_lexer()
tokens = lexer.lex(code)
for token in tokens:
    print(token)