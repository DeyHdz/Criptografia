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

  ### Flujo de ejecución (CLI)

1. Se solicita la **llave** y se construye la matriz (`crearMatriz`).
2. Se muestra la tabla (`printMatrix`).
3. Se solicita el **mensaje**.
4. El usuario elige **[1] Cifrar** o **[2] Descifrar**.
5. Se divide el mensaje en pares (`separador`).
6. Se ejecuta `cifrado` o `descifrado` y se muestra el resultado.
7. Se pregunta si desea continuar.

   ### Ejemplo de uso

   <img width="309" height="374" alt="image" src="https://github.com/user-attachments/assets/fe88e91a-f480-470f-b8c3-152d34e58ebe" />
   <img width="288" height="375" alt="image" src="https://github.com/user-attachments/assets/aa107b1e-b90a-4819-bd85-8e74915ecf5f" />

## Solución implementada (decisiones y objetivos)

- **Unificación I/J** para ajustar a 25 celdas. En todo el flujo, una `j` de entrada se trata como `i`.
- **Generación determinista de la tabla**: primero **llave sin duplicados**, luego **alfabeto restante** (sin `j`), en orden.
- **Separación en pares simple** con **relleno final 'x'** si el tamaño es impar.  
  - *Trade-off:* No se inserta `x` al **romper pares de letras iguales**. Esto simplifica la práctica y hace el flujo más transparente.
- **Reglas Playfair estándar** implementadas tanto para cifrado como para descifrado.
- **Interfaz CLI** mínima y clara para experimentar: ingresar llave, ver la tabla, introducir mensaje y escoger la operación.

## Notas importantes

- El programa **elimina espacios** y convierte todo a **minúsculas**.
- La letra **J** se trata como **I**. Al imprimir la tabla, se sugiere con `i/j` para mayor claridad visual.
- El programa utiliza aritmética modular para el wrap-around en la matriz
- Los caracteres especiales y números son eliminados en el preprocesamiento
- La llave debe contener solo letras (se procesan automáticamente)
- Para descifrar correctamente, se debe usar la misma llave utilizada para cifrar

## Aplicación de reglas:

- Columna: (renglón + 1) % 5 para cifrar, (renglón - 1) % 5 para descifrar
- Renglón: (columna + 1) % 5 para cifrar, (columna - 1) % 5 para descifrar
- Rectángulo: Intercambio de columnas (igual para cifrar y descifrar)


## Equipo 3

- Cruz Miranda Luis Eduardo
- De la Rosa Lara Gustavo
- Domínguez Ríos Luis Daniel
- Hernández Hernández Deissy Jovita
- Mendoza Rodríguez Ángel Jesús
- Nieto Rodríguez Tomás Andrés

