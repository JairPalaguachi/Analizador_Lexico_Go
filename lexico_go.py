"""
Analizador Léxico para el Lenguaje Go
Proyecto: Implementación de un Analizador Léxico en Go
Integrantes:
- Jair Palaguachi (JairPalaguachi)
- Javier Gutiérrez (SKEIILATT)
- Leonardo Macías (leodamac)
"""

import ply.lex as lex
from datetime import datetime
import sys
import os

# ============================================================================
# CONTRIBUCIÓN: Jair Palaguachi
# Sección: Palabras Reservadas y Tokens Básicos
# ============================================================================

# Palabras reservadas de Go
reserved = {
    'break': 'BREAK',
    'case': 'CASE',
    'chan': 'CHAN',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'default': 'DEFAULT',
    'defer': 'DEFER',
    'else': 'ELSE',
    'fallthrough': 'FALLTHROUGH',
    'for': 'FOR',
    'func': 'FUNC',
    'go': 'GO',
    'goto': 'GOTO',
    'if': 'IF',
    'import': 'IMPORT',
    'interface': 'INTERFACE',
    'map': 'MAP',
    'package': 'PACKAGE',
    'range': 'RANGE',
    'return': 'RETURN',
    'select': 'SELECT',
    'struct': 'STRUCT',
    'switch': 'SWITCH',
    'type': 'TYPE',
    'var': 'VAR',
}

# Lista de tokens
tokens = [
    # Identificadores y literales
    'ID',
    'INT_LITERAL',
    'FLOAT_LITERAL',
    'STRING_LITERAL',
    'RUNE_LITERAL',
    'BOOL_LITERAL',
    
    # Operadores aritméticos
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'INCREMENT',
    'DECREMENT',
    
    # Operadores de comparación
    'EQ',
    'NE',
    'LT',
    'LE',
    'GT',
    'GE',
    
    # Operadores lógicos
    'AND',
    'OR',
    'NOT',
    
    # Operadores de asignación
    'ASSIGN',
    'DECLARE_ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'TIMES_ASSIGN',
    'DIVIDE_ASSIGN',
    'MOD_ASSIGN',
    'AND_ASSIGN',
    'OR_ASSIGN',
    'XOR_ASSIGN',
    'LSHIFT_ASSIGN',
    'RSHIFT_ASSIGN',
    
    # Operadores bit a bit
    'BITAND',
    'BITOR',
    'BITXOR',
    'BITNOT',
    'LSHIFT',
    'RSHIFT',
    'AND_NOT',
    
    # Operadores de punteros y canales
    'ADDRESS',
    'POINTER',
    'CHANNEL_OP',
    
    # Delimitadores
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COMMA',
    'DOT',
    'COLON',
    'ELLIPSIS',
] + list(reserved.values())

# ============================================================================
# FIN CONTRIBUCIÓN: Jair Palaguachi
# ============================================================================


# ============================================================================
# CONTRIBUCIÓN COMPARTIDA: Manejo de Comentarios y Espacios
# ============================================================================

# Comentarios de una línea
def t_COMMENT_SINGLE(t):
    r'//[^\n]*'
    pass  # Los comentarios se ignoran

# Comentarios multilínea
def t_COMMENT_MULTI(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass  # Los comentarios se ignoran

# Saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    error_msg = f"Carácter ilegal '{t.value[0]}' en línea {t.lineno}, columna {find_column(t)}"
    print(error_msg)
    log_errors.append(error_msg)
    t.lexer.skip(1)

# ============================================================================
# FIN CONTRIBUCIÓN COMPARTIDA
# ============================================================================

# Función auxiliar para encontrar la columna
def find_column(token):
    line_start = lexer_data.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Variables globales para logging
log_tokens = []
log_errors = []
lexer_data = ""

# Construcción del lexer
lexer = lex.lex()

def analyze_file(filename):
    """
    Analiza un archivo de código Go y genera un log con los tokens encontrados.
    """
    global log_tokens, log_errors, lexer_data
    
    log_tokens = []
    log_errors = []
    
    # Leer el archivo
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
            lexer_data = data
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no fue encontrado.")
        return
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return
    
    # Reiniciar el lexer
    lexer.lineno = 1
    lexer.input(data)
    
    # Tokenizar
    print(f"\n{'='*80}")
    print(f"ANÁLISIS LÉXICO DEL ARCHIVO: {filename}")
    print(f"{'='*80}\n")
    
    token_count = 0
    while True:
        tok = lexer.token()
        if not tok:
            break
        
        token_count += 1
        column = find_column(tok)
        token_info = f"Token: {tok.type:20} | Valor: {str(tok.value):30} | Línea: {tok.lineno:4} | Columna: {column:4}"
        print(token_info)
        log_tokens.append(token_info)
    
    # Resumen
    print(f"\n{'='*80}")
    print(f"RESUMEN DEL ANÁLISIS")
    print(f"{'='*80}")
    print(f"Total de tokens reconocidos: {token_count}")
    print(f"Total de errores encontrados: {len(log_errors)}")
    
    if log_errors:
        print(f"\n{'='*80}")
        print(f"ERRORES ENCONTRADOS")
        print(f"{'='*80}")
        for error in log_errors:
            print(error)
    
    # Generar archivo de log
    generate_log(filename)

def get_git_username():
    """
    Obtiene el nombre de usuario de Git configurado localmente.
    Si no está configurado, retorna 'usuario'.
    """
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'config', 'user.name'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0 and result.stdout.strip():
            username = result.stdout.strip()
            username = username.replace(' ', '')
            return username
        else:
            return 'usuario'
    except:
        return 'usuario'

def generate_log(source_filename):
    """
    Genera un archivo de log con los tokens y errores encontrados.
    """
    # Crear carpeta de logs si no existe
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Obtener información del usuario de git
    git_user = get_git_username()
    
    # Generar nombre del archivo de log
    now = datetime.now()
    log_filename = f"logs/lexico-{git_user}-{now.strftime('%d-%m-%Y-%Hh%M')}.txt"
    
    # Escribir el log
    with open(log_filename, 'w', encoding='utf-8') as log_file:
        log_file.write("="*80 + "\n")
        log_file.write(f"ANÁLISIS LÉXICO - LENGUAJE GO\n")
        log_file.write("="*80 + "\n")
        log_file.write(f"Archivo analizado: {source_filename}\n")
        log_file.write(f"Fecha y hora: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
        log_file.write(f"Usuario: {git_user}\n")
        log_file.write("="*80 + "\n\n")
        
        log_file.write(f"TOKENS RECONOCIDOS ({len(log_tokens)})\n")
        log_file.write("-"*80 + "\n")
        for token in log_tokens:
            log_file.write(token + "\n")
        
        log_file.write("\n" + "="*80 + "\n")
        log_file.write(f"ERRORES LÉXICOS ({len(log_errors)})\n")
        log_file.write("-"*80 + "\n")
        if log_errors:
            for error in log_errors:
                log_file.write(error + "\n")
        else:
            log_file.write("No se encontraron errores léxicos.\n")
        
        log_file.write("\n" + "="*80 + "\n")
        log_file.write("FIN DEL ANÁLISIS\n")
        log_file.write("="*80 + "\n")
    
    print(f"\nLog generado exitosamente: {log_filename}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Cómo usar: python lexico_go.py <archivo.go>")
        print("Ejemplo de comando: python lexico_go.py algoritmo1.go")
        sys.exit(1)
    
    filename = sys.argv[1]
    analyze_file(filename)
