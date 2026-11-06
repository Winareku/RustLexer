# Analizador Léxico para Rust (PLY) - Lenguajes de Programación Grupo 11

| Integrante | Usuario Git | Aporte en `analizador_lexico.py` | Algoritmo de prueba |
|---|---|---|---|
| Windsor Estrada | @Winareku | Delimitadores, comentarios, newline/espacios | `algoritmos/algoritmo1.rs` |
| Israel Romero | @Madakase | Identificadores, macros, palabras reservadas, operadores | `algoritmos/algoritmo2.rs` |
| César Moreira | @MoreiraC18 | Literales y tipos de datos, tokens de error | `algoritmos/algoritmo3.rs` |

## Requisitos
Tener Python y Ejecutar `pip install -r requirements.txt`

## Objetivos
- Crear un analizador lexico, cada estudiante debe contribuir con componentes.
- Cada integrante debera usar su algoritmo de prueba asignado.
- Archivo main.py como punto central:
  ```
  # Ejemplo de Uso
  python main.py algoritmos/algoritmo1.rs Winareku
  ```
  Genera `logs/lexico-usuario-DD-MM-AAAA-HHhMM.txt` con tokens y errores.
