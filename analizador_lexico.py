import ply

# ------------------------------------------------------------
# Analizador Léxico para subconjunto de Rust
# ------------------------------------------------------------

import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'COMMA', 'SEMICOLON', 'COLON', 'DOT',

    'ID', 'RAW_ID', 'LOOP_LABEL', 'MACRO',

    'LET', 'MUT', 'CONST', 'STATIC', 'FN', 'STRUCT', 'ENUM', 'UNION',
    'TRAIT', 'IMPL', 'TYPE', 'IF', 'ELSE', 'MATCH', 'LOOP', 'WHILE',
    'FOR', 'IN', 'BREAK', 'CONTINUE', 'RETURN', 'TRUE', 'FALSE',
    'MOD', 'USE', 'CRATE', 'SUPER', 'SELF', 'SELF_TYPE', 'PUB', 'AS',
    'REF', 'MOVE', 'DYN', 'WHERE', 'ASYNC', 'AWAIT', 'UNSAFE', 'EXTERN',

    'STRING_LITERAL', 'CHAR_LITERAL', 'FLOAT_LITERAL', 'INTEGER_LITERAL', 'DATA_TYPE',

    'RANGE_INCLUSIVE', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULTIPLY_ASSIGN',
    'DIVIDE_ASSIGN', 'MODULO_ASSIGN', 'EQUAL', 'NOT_EQUAL', 'LESS_EQUAL',
    'GREATER_EQUAL', 'AND', 'OR', 'RANGE', 'PATHSEP', 'ARROW', 'FAT_ARROW',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO', 'LESS_THAN',
    'GREATER_THAN', 'NOT', 'ASSIGN', 'AMPERSAND', 'PIPE'
)

# =============================================================
# Windsor Estrada: Delimitadores, Comentarios y Saltos de línea
# =============================================================

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COMMA     = r','
t_SEMICOLON = r';'
t_COLON     = r':'
t_DOT       = r'\.'

def t_COMMENT_LINE(t):
    r'//.*'
    pass

def t_COMMENT_BLOCK(t):
    r'/\*[^*]*\*+([^/][^*]*\*+)*/'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

# ===========================================================
# Cesar: Literales (números, strings, char) y Tipos de datos.
# ===========================================================

def t_STRING_LITERAL(t):
    r'"([^"\\\n]|\\.)*"'
    return t

def t_CHAR_LITERAL(t):
    r"'([^'\\\n]|\\.)'"
    return t

def t_FLOAT_LITERAL(t):
    r'(?:[0-9][0-9_]*\.[0-9][0-9_]*(?:[eE][+-]?[0-9][0-9_]*)?|[0-9][0-9_]*[eE][+-]?[0-9][0-9_]*)(?:f32|f64)?|[0-9][0-9_]*(?:f32|f64)'
    return t

def t_INTEGER_LITERAL(t):
    r'(?:0[xX][0-9a-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|[0-9][0-9_]*)(?:i8|i16|i32|i64|i128|isize|u8|u16|u32|u64|u128|usize)?'
    return t

# ==========================================================
# Israel: Identificadores, Palabras Reservadas y Operadores.
# ==========================================================

reserved = {
    'let': 'LET', 'mut': 'MUT', 'const': 'CONST', 'static': 'STATIC',
    'fn': 'FN', 'struct': 'STRUCT', 'enum': 'ENUM', 'union': 'UNION',
    'trait': 'TRAIT', 'impl': 'IMPL', 'type': 'TYPE', 'if': 'IF',
    'else': 'ELSE', 'match': 'MATCH', 'loop': 'LOOP', 'while': 'WHILE',
    'for': 'FOR', 'in': 'IN', 'break': 'BREAK', 'continue': 'CONTINUE',
    'return': 'RETURN', 'true': 'TRUE', 'false': 'FALSE', 'mod': 'MOD',
    'use': 'USE', 'crate': 'CRATE', 'super': 'SUPER', 'self': 'SELF',
    'Self': 'SELF_TYPE', 'pub': 'PUB', 'as': 'AS', 'ref': 'REF',
    'move': 'MOVE', 'dyn': 'DYN', 'where': 'WHERE', 'async': 'ASYNC',
    'await': 'AWAIT', 'unsafe': 'UNSAFE', 'extern': 'EXTERN',
    'i8': 'DATA_TYPE', 'i16': 'DATA_TYPE', 'i32': 'DATA_TYPE', 'i64': 'DATA_TYPE',
    'i128': 'DATA_TYPE', 'isize': 'DATA_TYPE', 'u8': 'DATA_TYPE', 'u16': 'DATA_TYPE',
    'u32': 'DATA_TYPE', 'u64': 'DATA_TYPE', 'u128': 'DATA_TYPE', 'usize': 'DATA_TYPE',
    'f32': 'DATA_TYPE', 'f64': 'DATA_TYPE', 'bool': 'DATA_TYPE', 'char': 'DATA_TYPE',
    'str': 'DATA_TYPE', 'String': 'DATA_TYPE',
}

# IDENTIFICADORES
def t_RAW_ID(t):
    r'r\#[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*(!(?!=))?'
    if t.value.endswith('!'):
        t.type = 'MACRO'
    else:
        t.type = reserved.get(t.value, 'ID')
    return t

t_LOOP_LABEL = r"'[a-zA-Z_][a-zA-Z0-9_]*"

# Operadores compuestos (varios caracteres)
t_RANGE_INCLUSIVE = r'\.\.='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MODULO_ASSIGN = r'%='
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_RANGE = r'\.\.'
t_PATHSEP = r'::'
t_ARROW = r'->'
t_FAT_ARROW = r'=>'

# Operadores simples (un solo carácter)
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_LESS_THAN = r'<'
t_GREATER_THAN = r'>'
t_NOT = r'!'
t_ASSIGN = r'='
t_AMPERSAND = r'&'
t_PIPE = r'\|'

# Manejo de errores léxicos global
def t_error(t):
    caracter = t.value[0]
    t.lexer.errores.append({'linea': t.lexer.lineno, 'mensaje': f"Carácter no reconocido {caracter!r}"})
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

def analizar(codigo):
    lexer.lineno = 1
    lexer.errores = []
    lexer.input(codigo)

    tokens_encontrados = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_encontrados.append({
            'tipo': tok.type,
            'valor': tok.value,
            'linea': tok.lineno,
            'columna': find_column(codigo, tok)
        })
    return tokens_encontrados, lexer.errores

def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        return token.lexpos + 1
    return (token.lexpos - last_cr)
