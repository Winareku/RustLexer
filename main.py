# ------------------------------------------------------------
# main.py - Ejecuta el analizador léxico y genera el log
# ------------------------------------------------------------

# Uso: python main.py algoritmos/algoritmo1.rs Winareku

import os
import sys
from datetime import datetime
from analizador_lexico import analizar

def main():
    if len(sys.argv) != 3:
        print("Uso: python main.py <archivo.rs> <usuarioGit>")
        sys.exit(1)

    ruta, usuario = sys.argv[1], sys.argv[2]
    
    try:
        with open(ruta, encoding='utf-8') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'")
        sys.exit(1)

    ahora = datetime.now()
    tokens, errores = analizar(codigo)

    lineas = [
        "ANALIZADOR LÉXICO - RUST (PLY)",
        f"Archivo analizado : {ruta}",
        f"Usuario Git       : {usuario}",
        f"Fecha y hora      : {ahora.strftime('%d/%m/%Y %H:%M:%S')}",
        "",
        "=== TOKENS RECONOCIDOS ===",
        f"{'LÍNEA':<7}{'COL':<6}{'TIPO':<14}VALOR",
        "-" * 50,
    ]
    for t in tokens:
        lineas.append(f"{t['linea']:<7}{t['columna']:<6}{t['tipo']:<14}{t['valor']!r}")

    lineas += ["", "=== ERRORES LÉXICOS ==="]
    if errores:
        for e in errores:
            lineas.append(f"[ERROR] Línea {e['linea']}, Columna {e['columna']}: {e['mensaje']}")
    else:
        lineas.append("(ninguno)")

    lineas += ["", "=== RESUMEN ===",
               f"Tokens reconocidos: {len(tokens)}",
               f"Errores léxicos   : {len(errores)}"]
    texto = "\n".join(lineas) + "\n"

    os.makedirs("logs", exist_ok=True)
    nombre = f"lexico-{usuario}-{ahora.strftime('%d-%m-%Y-%Hh%M')}.txt"
    destino = os.path.join("logs", nombre)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(texto)

    print(texto)
    print(f"Log guardado exitosamente en: {destino}")

if __name__ == "__main__":
    main()
