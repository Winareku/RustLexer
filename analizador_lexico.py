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
