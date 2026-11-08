import ply

# ------------------------------------------------------------
# Analizador Léxico para subconjunto de Rust
# ------------------------------------------------------------

import ply.lex as lex

# Lista de Tareas:
# Windsor - Delimitadores
# Israel - Identificadores, Palabras Reservadas y Operadores
# Cesar - Literales y Tipos de Datos

# Lista de nombres de tokens
tokens = (
    # Se irán agregando los tokens de todo el equipo aquí
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'DOT',

    'ID',
    'RAW_ID',
    'LOOP_LABEL',
    'MACRO',

    'LET',
    'MUT',
    'CONST',
    'STATIC',
    'FN',
    'STRUCT',
    'ENUM',
    'UNION'
    'TRAIT',
    'IMPL',
    'TYPE',
    'IF',
    'ELSE',
    'MATCH',
    'LOOP',
    'WHILE',
    'FOR',
    'IN',
    'BREAK',
    'CONTINUE',
    'RETURN',
    'TRUE',
    'FALSE',
    'MOD',
    'USE',
    'CRATE',
    'SUPER',
    'SELF',
    'SELF_TYPE',
    'PUB',
    'AS',
    'REF',
    'MOVE',
    'DYN',
    'WHERE',
    'ASYNC',
    'AWAIT',
    'UNSAFE',
    'EXTERN',

    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULO',

    'EQUAL',
    'NOT_EQUAL',
    'LESS_THAN',
    'GREATER_THAN',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'PIPE',

    'AND',
    'OR',
    'NOT',

    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'MULTIPLY_ASSIGN',
    'DIVIDE_ASSIGN',
    'MODULO_ASSIGN',

    'RANGE',
    'RANGE_INCLUSIVE',
    'AMPERSAND',
    'PATHSEP',
    'ARROW',
    'FAT_ARROW',
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
    pass  # Ignorar comentarios de línea

def t_COMMENT_BLOCK(t):
    r'/\*[^*]*\*+([^/][^*]*\*+)*/'
    pass  # Ignorar comentarios de bloque

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

# ==========================================================
# Israel: Identificadores, Palabras Reservadas y Operadores.
# ==========================================================

# PALABRAS RESERVADAS
reserved = {
    'let': 'LET',
    'mut': 'MUT',
    'const': 'CONST',
    'static': 'STATIC',
    'fn': 'FN',
    'struct': 'STRUCT',
    'enum': 'ENUM',
    'union': 'UNION',
    'trait': 'TRAIT',
    'impl': 'IMPL',
    'type': 'TYPE',
    'if': 'IF',
    'else': 'ELSE',
    'match': 'MATCH',
    'loop': 'LOOP',
    'while': 'WHILE',
    'for': 'FOR',
    'in': 'IN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
    'true': 'TRUE',
    'false': 'FALSE',
    'mod': 'MOD',
    'use': 'USE',
    'crate': 'CRATE',
    'super': 'SUPER',
    'self': 'SELF',
    'Self': 'SELF_TYPE',
    'pub': 'PUB',
    'as': 'AS',
    'ref': 'REF',
    'move': 'MOVE',
    'dyn': 'DYN',
    'where': 'WHERE',
    'async': 'ASYNC',
    'await': 'AWAIT',
    'unsafe': 'UNSAFE',
    'extern': 'EXTERN'
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

# OPERADORES CON VARIOS CARACTERES
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

# OPERADORES CON SOLO UN CARACTER
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

# ===========================================================
# Cesar: Literales (números, strings, char) y Tipos de datos.
# ===========================================================


# Manejo de errores léxicos global
def t_error(t):
    print(f"Error léxico: Carácter no reconocido '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

def analizar(codigo):
    lexer.input(codigo)
    tokens_encontrados = []
    errores_encontrados = []
    
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
    return tokens_encontrados, errores_encontrados

def find_column(input_text, token):
    last_cr = input_text.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        return token.lexpos + 1
    return (token.lexpos - last_cr)
