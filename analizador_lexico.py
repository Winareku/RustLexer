import ply

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------

import ply.lex as lex

reserved = {
"_print":"PRINT",
"_if": "IF",
"_else": "ELSE",
"_while": "WHILE",
"_for": "FOR",
"_return": "RETURN",
"_def": "DEF"
}

# List of token names. This is always required
tokens = (
'NUMBER',
'PLUS',
'MINUS',
'TIMES',
'DIVIDE',
'LPAREN',
'RPAREN',
'MOD',
'VARIABLE',
'FLOAT'
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'

# A regular expression rule with some action code
def t_VARIABLE(t):
r'_[a-z]\w*'
t.type = reserved.get(t.value, 'VARIABLE')
return t

def t_FLOAT(t):
r"\d+\.\d+"
t.value = float(t.value)
return t

def t_NUMBER(t):
r'\d+'
t.value = int(t.value)
return t

# Define a rule so we can track line numbers
def t_newline(t):
r'\n+'
t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
print(f"Caracter no definido en el lenguaje {t.value[0]}")
t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10 if _nombreVar
+ -20 *2 _print _while 9.4
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
tok = lexer.token()
if not tok:
break # No more input
print(tok)
