# Cifrado Vigenère en Python

## Descripción

Este proyecto implementa el algoritmo de **Cifrado Vigenère**, un cifrado por sustitución poligráfico que utiliza una **llave** repetitiva para cifrar un mensaje. 
A diferencia del Cifrado César, el Cifrado Vigenère varía el **desplazamiento** de cada letra en función de la letra correspondiente de la llave.

## Características

- ✅ Soporta tanto **cifrado** como **descifrado** de texto
- ✅ La **llave** se ajusta para coincidir con la longitud del mensaje
- ✅ Funciones que manejan **mayúsculas** y **minúsculas**
- ✅ Los caracteres no alfabéticos (espacios, puntuaciones) permanecen inalterados
- ✅ Función de **criptoanálisis**: permite analizar texto cifrado y determinar la longitud probable de la clave usando el **método de Kasiski**
- ✅ Interfaz de **línea de comandos** interactiva

## ¿Cómo funciona el Cifrado Vigenère?

El Cifrado Vigenère utiliza una **clave** que se repite a lo largo del mensaje. Cada letra del mensaje se cifra utilizando el valor de la letra correspondiente en la clave.

### Proceso de Cifrado:
1. **Llave ajustada**: Si la longitud de la llave es menor que la del mensaje, se repite hasta que tenga la misma longitud.
2. **Desplazamiento**: El valor de cada letra de la llave determina el desplazamiento de la letra correspondiente en el mensaje. Por ejemplo, A=0, B=1, C=2, etc.
3. **Cifrado**: Para cada letra del mensaje, se aplica el desplazamiento correspondiente de la clave.

### Proceso de Descifrado:
- El proceso de descifrado es la **inversa** del cifrado, usando el desplazamiento negativo correspondiente.

## Análisis de Kasiski

El **método de Kasiski** es una técnica de **criptoanálisis** que permite estimar la **longitud de la clave** usada en un cifrado Vigenère, sin conocer la clave. Funciona así:

1. **Buscar repeticiones de secuencias**:
   - Se identifican secuencias de **3 a 5 letras** que se repiten en el texto cifrado.
   - Solo se consideran aquellas secuencias que aparecen más de una vez.

2. **Medir distancias entre repeticiones**:
   - Para cada secuencia repetida, se calcula la **distancia (en número de caracteres)** entre sus apariciones.

3. **Calcular divisores comunes**:
   - Se analiza cada distancia y se buscan sus **divisores enteros**.
   - Los divisores más frecuentes son **candidatos a ser la longitud de la llave**, porque la clave se repite cada cierto número de caracteres.

4. **Sugerir longitudes de clave**:
   - El programa muestra un **ranking de longitudes candidatas**, de mayor a menor frecuencia.
   - Esto permite al usuario intentar descifrar el mensaje usando la longitud de clave sugerida.

> 🔹 Nota: Para que el análisis funcione correctamente, el mensaje cifrado debe ser suficientemente largo y contener **repeticiones de patrones** que generen secuencias cifradas idénticas.


## Estructura del código

### Funciones principales

- **`desplazar_caracter(caracter, corrimiento)`**: Desplaza un carácter individual según el corrimiento especificado.
- **`cifrar(palabra, corrimiento)`**: Cifra una palabra o frase completa utilizando el corrimiento de la clave.
- **`decifrar(palabra, corrimiento)`**: Descifra una palabra o frase previamente cifrada.
- **`ajustar_llave(key, mensaje)`**: Ajusta la llave para que tenga la misma longitud que el mensaje, replicándola si es necesario.
- **`solo_letras(texto)`**: Filtra y convierte el texto a **mayúsculas**, eliminando caracteres no alfabéticos.
- **`dividir_columnas(ciphertext, key_len)`**: Divide el texto cifrado en columnas, según la longitud de la llave.
- **`encontrar_repeticiones(texto)`**: Busca repeticiones en el texto cifrado que puedan ayudar a determinar la longitud de la clave (para el análisis de Kasiski).
- **`contar_divisores(distancias)`**: Cuenta los divisores de las distancias encontradas en el análisis de Kasiski.

### Flujo de ejecución (CLI)

1. El usuario elige entre **cifrado** o **descifrado**.
2. Se ingresa la **palabra o frase** que se desea cifrar/descifrar.
3. El usuario ingresa la **llave**, la cual será ajustada a la longitud del mensaje.
4. El sistema aplica el cifrado o descifrado y muestra el resultado.
5. El usuario puede elegir entre realizar otra operación o salir.

## Ejemplo de uso

### Algoritmo criptográfico
<img width="308" height="393" alt="image" src="https://github.com/user-attachments/assets/ec1118a8-7e99-4289-87fa-28cd3e62d206" />
<img width="308" height="393" alt="image" src="https://github.com/user-attachments/assets/8fe4026d-11fa-4379-99b2-811792533dc5" />

### Algoritmo criptoanálisis
<img width="295" height="379" alt="image" src="https://github.com/user-attachments/assets/8c7b8399-ad65-4cf6-acf8-1e3e81e69a89" />
<img width="401" height="276" alt="image" src="https://github.com/user-attachments/assets/4b8ae8d0-2297-47ef-be22-c3a5c6122f06" />


## Notas importantes

- El programa maneja mayúsculas y minúsculas.
- Los caracteres no alfabéticos son ignorados (espacios, puntuaciones, etc.).
- El análisis de Kasiski permite obtener la longitud probable de la clave.
- Este algoritmo es más seguro que el Cifrado César, pero aún vulnerable a criptoanálisis en casos modernos.


  ## Equipo 3

- Cruz Miranda Luis Eduardo
- De la Rosa Lara Gustavo
- Domínguez Ríos Luis Daniel
- Hernández Hernández Deissy Jovita
- Mendoza Rodríguez Ángel Jesús
- Nieto Rodríguez Tomás Andrés


