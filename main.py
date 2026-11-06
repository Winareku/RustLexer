# ------------------------------
# Borrador del Analizador Léxico
# ------------------------------

import sys
from analizador_lexico import analizar

def main():

    # Validar que se envíe el archivo por consola
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.rs")
        sys.exit(1)

    ruta_archivo = sys.argv[1]

    # Leer el archivo
    try:
        with open(ruta_archivo, encoding='utf-8') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
        sys.exit(1)

    # Uso del analizador léxico
    tokens, errores = analizar(codigo)

    # Mostrar resultados
    print(f"\nResultados para {ruta_archivo} ({len(tokens)} tokens):")
    for t in tokens:
        print(f"  Línea {t['linea']}: {t['tipo']} -> {t['valor']!r}")

    if errores:
        print("\nErrores encontrados:")
        for e in errores:
            print(f"  Línea {e['linea']}: {e['mensaje']}")
    else:
        print("\nAnálisis completado sin errores.")

if __name__ == "__main__":
    main()
