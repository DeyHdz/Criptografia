# Cifrado César en Python

## Descripción

Este proyecto implementa el algoritmo clásico de **Cifrado Wheatstone**, es un cifrado por sustitución poligráfica que utiliza una tabla (matriz) de 5×5 y convierte el texto en pares de letras para cifrarlo siguiendo reglas basadas en la posición en la matriz.

## Características

- ✅ Cifrado poligráfico, es decir, no trabaja con letras individuales, sino con pares de letras (dígrafos).
- ✅ Basado en una clave, esta define la organización de las letras y, por tanto, el resultado del cifrado.
- ✅ Uso de una matriz reducida (25 letras)
- ✅ No es monoalfabético, por lo que una misma letra puede cifrarse de distintas formas, dependiendo de la letra que la acompañe.


## Cómo funciona el Cifrado César

El cifrado César desplaza cada letra del alfabeto un número determinado de posiciones. Por ejemplo, con un corrimiento de 3:

- A → D
- B → E  
- C → F
- ...
- X → A (vuelve al inicio)
- Y → B
- Z → C

## Estructura del código

### Alfabetos utilizados
```python
alfabeto_minus = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
```

### Funciones principales

- **`desplazar_caracter(caracter, corrimiento)`**: Desplaza un carácter individual según el corrimiento especificado
- **`cifrar(palabra, corrimiento)`**: Cifra una palabra o frase completa
- **`decifrar(palabra, corrimiento)`**: Descifra una palabra o frase previamente cifrada

## Uso del programa

1. Ejecuta el archivo Python
2. Ingresa la palabra o frase que deseas procesar
3. Selecciona la operación:
   - **[1]** para cifrar
   - **[2]** para descifrar
4. Introduce el número de corrimiento (puede ser positivo o negativo)
5. Obtén el resultado
6. Decide si quieres realizar otra operación

## Ejemplo de uso

```
===== CIFRADO CESAR =====
Escribe la palabra o frase:
> Hola Mundo!

Elige:
[1] Cifrar
[2] Decifrar
> 1

Corrimiento (número entero):
> 3

Resultado: Krod Pxqgr!

¿Quieres hacer otra operación? (s/n): n
Saliendo del programa...
```

## Requisitos

- Python 3
- No se requieren librerías adicionales

## Instalación y ejecución

1. Clona o descarga el archivo `cifrado_cesar.py`
2. Abre una terminal en el directorio del archivo
3. Ejecuta el comando:
   ```bash
   python cifrado_cesar.py
   ```

## Notas importantes

- El programa utiliza aritmética modular para manejar el "wrap-around" del alfabeto
- Los caracteres que no son letras (números, espacios, signos de puntuación) permanecen sin cambios
- El corrimiento puede ser cualquier número entero (positivo o negativo)
- Para descifrar, se utiliza el corrimiento negativo del valor original


## Equipo 3
- Cruz Miranda Luis Eduardo
- Domínguez Ríos Luis Daniel
- Hernández Hernández Deissy Jovita

Proyecto desarrollado como ejercicio de clase de Criptografía.
