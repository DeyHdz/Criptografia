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

## Requisitos

- Python 3.x
- No se requieren librerías adicionales.

## Instalación y ejecución

1. Clona o descarga este archivo `Practica2_CifradoVigenere.py`.
2. Abre una terminal en el directorio del archivo.
3. Ejecuta el comando:
   ```bash
   python Practica2_CifradoVigenere.py

## Notas importantes

- El programa maneja mayúsculas y minúsculas.
- Los caracteres no alfabéticos son ignorados (espacios, puntuaciones, etc.).
- El análisis de Kasiski permite obtener la longitud probable de la clave.
- Este algoritmo es más seguro que el Cifrado César, pero aún vulnerable a criptoanálisis en casos modernos.

  

