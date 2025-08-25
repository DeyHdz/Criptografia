# Cifrado Wheatstone en Python

## Descripción

Este proyecto implementa el algoritmo clásico de **Cifrado Wheatstone**, una técnica de cifrado **poligráfico** que trabaja con **pares de letras (dígrafos)** y utiliza una **matriz 5×5** generada a partir de una palabra o frase **llave**. En esta implementación se unifican las letras **I/J**, para completar las 25 posiciones de la tabla.

## Características

- ✅ Cifrado y descifrado por **pares de letras** (dígrafos).
- ✅ Construcción de la **matriz 5×5** a partir de una **llave** definida por el usuario.
- ✅ **Unificación I/J**: la **J** se trata como **I**.
- ✅ Eliminación automática de **espacios** y conversión a **minúsculas** para el proceso.
- ✅ Interfaz de **línea de comandos** interactiva.
- ✅ Implementación de las **tres reglas de Playfair**: misma fila, misma columna y rectángulo.
- ✅ Impresión de la **tabla** generada para verificación visual.


## ¿Cómo funciona el Cifrado Wheatstone (Playfair)?

1. **Tabla 5×5 (clave):**
   - Se toma la llave (palabra/frase), se eliminan repeticiones y se colocan sus letras en la matriz.
   - Se completa con el resto del alfabeto (sin **j**) hasta llenar 25 casillas.
   - La **J** se mapea a **I** durante todo el proceso.

2. **Preparación del mensaje:**
   - Se eliminan espacios y se convierten a minúsculas.
   - El mensaje se divide en **pares**. Si el total es impar, se **rellena con 'x'**.
   - *(Limitación actual)*: esta versión **no** inserta automáticamente una letra de relleno cuando un par contiene **letras iguales** (p.ej., “ll”). Ver **Mejoras/Extensiones**.

3. **Reglas de sustitución (por cada par):**
   - **Misma columna →** se toma la letra **debajo** (con desplazamiento circular).
   - **Misma fila →** se toma la letra de la **derecha** (con desplazamiento circular).
   - **Rectángulo →** se toman las letras en las **esquinas** del rectángulo formado, manteniendo las filas originales e intercambiando columnas.

## Estructura del código

### Archivos
- `Practica3_CifradoWheatstone.py` — Implementación completa e interfaz CLI.

### Funciones principales

- `crearMatriz()`  
  Construye y devuelve la **matriz 5×5** según la `llave` global:
  - Recorre la llave, evita duplicados, unifica `j → i`.
  - Completa con el alfabeto `abcdefghiklmnopqrstuvwxyz` (sin `j`).

- `printMatrix(matriz)`  
  Imprime la matriz en consola. Muestra `i/j` cuando corresponde para indicar la unificación.

- `getRenglonColumna(c, matriz)`  
  Devuelve `(fila, columna)` de la letra `c` en `matriz`. Si `c == 'j'`, busca la posición de `'i'`.

- `getCaracter(i, j, matriz)`  
  Devuelve el carácter en la posición `(i, j)` de la matriz.

- `separador(mensaje)`  
  Limpia y separa el texto en **pares**. Si el tamaño es impar, **agrega 'x'** al final.
  > *Nota:* No divide pares con letras repetidas (p. ej., `ll`).

- `cifrado(mensaje_separado, matriz)`  
  Aplica las **reglas Playfair** para **cifrar** cada par.

- `descifrado(mensaje_separado, matriz)`  
  Aplica las reglas inversas para **descifrar** cada par.
