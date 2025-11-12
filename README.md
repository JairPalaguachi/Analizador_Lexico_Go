# Analizador Léxico para Go

## Proyecto: Implementación de un Analizador Léxico, Sintáctico y Semántico en Go

### Integrantes
- **Jair Palaguachi** - Usuario GitHub: JairPalaguachi
- **Javier Gutiérrez** - Usuario GitHub: SKEIILATT
- **Leonardo Macías** - Usuario GitHub: leodamac

### PAO: 2025 - II
### Profesora: Fanny Cisneros Carlota

---

## Descripción del Proyecto

Este proyecto implementa un analizador léxico completo para el lenguaje de programación Go utilizando PLY (Python Lex-Yacc). El analizador es capaz de:

- Identificar y clasificar todos los tokens del lenguaje Go
- Reconocer palabras reservadas, operadores, identificadores, literales y delimitadores
- Generar mensajes de error personalizados para caracteres no reconocidos
- Crear logs detallados de los tokens identificados

---

## Estructura del Repositorio

```
Analizador_Lexico_Go/
│
├── lexico_go.py           # Analizador léxico principal
├── algoritmo1.go          # Algoritmo de prueba (Jair Palaguachi)
├── algoritmo2.go          # Algoritmo de prueba (Javier Gutiérrez)
├── algoritmo3.go          # Algoritmo de prueba (Leonardo Macías)
├── logs/                  # Directorio para archivos de log
│   └── (archivos .txt)    # Logs generados automáticamente
├── README.md              # Este archivo
└── requirements.txt       # Dependencias de Python
```

---

## Requisitos Previos

### Software Necesario
- Python 3.7 o superior
- PLY (Python Lex-Yacc)

### Instalación de Dependencias

```bash
# Crear un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar PLY
pip install ply
```

O usando el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

---

## Uso del Analizador

### Comando Básico

```bash
python lexico_go.py <archivo.go>
```

### Ejemplos

```bash
# Analizar el algoritmo 1
python lexico_go.py algoritmo1.go

# Analizar el algoritmo 2
python lexico_go.py algoritmo2.go

# Analizar el algoritmo 3
python lexico_go.py algoritmo3.go
```

### Salida del Programa

El programa genera dos tipos de salida:

1. **Salida en consola**: Muestra todos los tokens identificados en tiempo real
2. **Archivo de log**: Se guarda automáticamente en el directorio `logs/`

---

## Formato del Archivo de Log

Los archivos de log se generan con el siguiente formato de nombre:

```
lexico-<usuario>-<dd-mm-yyyy-HHhMM>.txt
```

Ejemplo: `lexico-JairPalaguachi-11-11-2025-14h32.txt`

### Contenido del Log

```
================================================================================
ANÁLISIS LÉXICO - LENGUAJE GO
================================================================================
Archivo analizado: algoritmo1.go
Fecha y hora: 11/11/2025 14:32:15
Usuario: JairPalaguachi
================================================================================

TOKENS RECONOCIDOS (156)
--------------------------------------------------------------------------------
Token: PACKAGE              | Valor: package                        | Línea:    1 | Columna:    1
Token: ID                   | Valor: main                           | Línea:    1 | Columna:    9
...

================================================================================
ERRORES LÉXICOS (0)
--------------------------------------------------------------------------------
No se encontraron errores léxicos.

================================================================================
FIN DEL ANÁLISIS
================================================================================
```

---

## Componentes del Analizador

### Tokens Reconocidos

El analizador identifica los siguientes tipos de tokens:

#### 1. Palabras Reservadas (25 palabras)
```
break, case, chan, const, continue, default, defer, else, fallthrough, 
for, func, go, goto, if, import, interface, map, package, range, return, 
select, struct, switch, type, var
```

#### 2. Identificadores
- Variables: `nombre`, `edad`, `_temp`, `contador1`
- Funciones: `calcular`, `procesarDatos`

#### 3. Literales
- **Enteros**: `42`, `100`, `0`
- **Flotantes**: `3.14`, `2.5e10`, `0.001`
- **Cadenas**: `"Hola Mundo"`, `"Go lang"`
- **Runas**: `'A'`, `'♥'`, `'\n'`
- **Booleanos**: `true`, `false`

#### 4. Operadores
- **Aritméticos**: `+`, `-`, `*`, `/`, `%`, `++`, `--`
- **Comparación**: `==`, `!=`, `<`, `<=`, `>`, `>=`
- **Lógicos**: `&&`, `||`, `!`
- **Asignación**: `=`, `:=`, `+=`, `-=`, `*=`, `/=`, `%=`
- **Bit a bit**: `&`, `|`, `^`, `<<`, `>>`, `&^`
- **Especiales**: `&` (dirección), `*` (puntero), `<-` (canal)

#### 5. Delimitadores
```
( ) { } [ ] ; , . : ...
```

---



## Algoritmos de Prueba

### Algoritmo 1 - Jair Palaguachi
**Enfoque**: Declaraciones de Variables
- Declaración con `var` y tipo explícito
- Declaración con inferencia de tipo
- Declaración corta (`:=`)
- Declaración múltiple
- Bloques de declaración
- Constantes
- Operadores aritméticos básicos

### Algoritmo 2 - Javier Gutiérrez
**Enfoque**: Estructuras de Control
- Condicionales `if-else`
- Condicionales con `else if`
- Expresiones booleanas compuestas
- Bucles `for` (tradicional, estilo while, con range)
- Switch básico y sin expresión
- Operadores de comparación

### Algoritmo 3 - Leonardo Macías
**Enfoque**: Estructuras de Datos y Funciones
- Arreglos de tamaño fijo
- Slices (arreglos dinámicos)
- Mapas (diccionarios)
- Funciones simples y con múltiples retornos
- Funciones con retornos nombrados
- Funciones variádicas
- Operaciones con punteros
- Operadores bit a bit

---

## Características Especiales

### Manejo de Comentarios
El analizador ignora correctamente:
- Comentarios de una línea: `// comentario`
- Comentarios multilínea: `/* comentario */`

### Detección de Errores
- Identifica caracteres ilegales
- Reporta la línea y columna exacta del error
- Proporciona mensajes descriptivos

### Seguimiento de Posición
- Número de línea preciso
- Cálculo de columna para cada token
- Información útil para debugging

---

## Ejecución de Pruebas

### Prueba Completa de los 3 Algoritmos

```bash
# Ejecutar todos los algoritmos
python lexico_go.py algoritmo1.go
python lexico_go.py algoritmo2.go
python lexico_go.py algoritmo3.go
```

### Verificación de Logs

Después de ejecutar las pruebas, se pueden verificar los logs generados:

```bash
ls -l logs/
```

Se visualizará algo como:
```
lexico-JairPalaguachi-11-11-2025-14h30.txt
lexico-SKEIILATT-11-11-2025-14h31.txt
lexico-leodamac-11-11-2025-14h32.txt
```

---

## Solución de Problemas comunes

### Error: "No module named 'ply'"
```bash
pip install ply
```

### Error: "File not found"
Asegurarse de que el archivo `.go` esté en el mismo directorio que `lexico_go.py` o proporcionar la ruta completa:
```bash
python lexico_go.py ruta/al/archivo.go
```


## Referencias

- [The Go Programming Language Specification](https://go.dev/ref/spec)
- [PLY (Python Lex-Yacc) Documentation](https://www.dabeaz.com/ply/ply.html)
- [Go by Example](https://gobyexample.com)

---

## Licencia

Este proyecto es parte de un trabajo académico para el curso de Lenguajes de Programación.

**Universidad**: ESPOL  
**Curso**: Lenguajes de Programación  
**Profesora**: Fanny Cisneros Carlota  
**PAO**: 2025 - II

---


