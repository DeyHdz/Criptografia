# Cifrado Vernam 

## Descripción

El cifrado de Vernam es un método de cifrado simétrico basado en la operación lógica XOR (⊕) entre el mensaje original y una clave aleatoria de igual longitud. Cuando la clave es realmente aleatoria, usada una sola vez y mantenida en secreto, se conoce como One-Time Pad (OTP).

El programa implementa el algoritmo en Python, con un menú interactivo que permite al usuario cifrar y descifrar mensajes utilizando un alfabeto definido que incluye letras (mayúsculas, minúsculas), números y varios símbolos.

## Características
- Definición de un alfabeto extendido que incluye letras, dígitos y caracteres especiales.
- Generación aleatoria de claves de la misma longitud que el mensaje.
- Operación de cifrado y descifrado mediante XOR bit a bit.
- Almacenamiento del mensaje cifrado en CM.txt y de la clave en K.txt.
- Eliminación de los archivos después del descifrado, garantizando seguridad.
- Interfaz de línea de comandos interactiva.

## ¿Cómo funciona el cifrado Vernam?

1. Definición del alfabeto. 
    - Se establece un conjunto de caracteres válidos. Cada símbolo tiene un índice asociado en la lista abecedario

2. Cifrado
    - Se recibe el mensaje y se obtiene la longitud. 
    - Se convierte cada carácter del mensaje en su valor numérico.
    - Se genera una clave aleatoria de igual longitud.
    - Se aplica la operación XOR: c = p⊕k
    - El resultado se guarda en CM.txt y la clave en K.txt.

3. Descifrado
    - Se lee el mensaje cifrado y la clave desde los archivos.
    - Se aplica de nuevo la operación XOR carácter por carácter: p = c⊕k
    - Se reconstruye el mensaje original y se muestran los resultados.
    - Se eliminan los archivos CM.txt y K.txt.


## Estructura del código

### Alfabeto utilizado

``` python3
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789.,;:!?()[]{}<>@#$%^&*-_+=/\\|\"' "
```

### Funciones principales

- **charToInt(character)**: Devuelve el índice de un carácter dentro del alfabeto.
- **IntToChar(integer)**: Convierte un índice numérico en el carácter correspondiente.
- **random_number()**: Genera un número aleatorio válido dentro del rango del alfabeto.
- **cifrar()**: Implementa el proceso de cifrado. Guarda mensaje cifrado y clave en archivos.
- **descifrar()**: Implementa el proceso de descifrado. Reconstruye el mensaje y elimina los archivos.

### Archivos generados

- CM.txt — Mensaje cifrado.
- K.txt — Clave generada.


## Ejemplo de uso

``` python3
=== MENÚ ===
1. Cifrar mensaje   
2. Descifrar mensaje
3. Salir
> 1

Escribe tu mensaje:
> HOLA MUNDO

Key guardada en: K.txt
Mensaje cifrado guardado en: CM.txt

=== MENÚ ===
1. Cifrar mensaje
2. Descifrar mensaje
3. Salir
> 2

=== Modo Descifrado ===
Tu mensaje cifrado está en CM.txt y la clave en K.txt. ¿Estás listo para descifrar? (s/n)
> s

Mensaje descifrado:
HOLA MUNDO

Archivos CM.txt y K.txt eliminados.

=== MENÚ ===
1. Cifrar mensaje
2. Descifrar mensaje
3. Salir
> 3

Saliendo...
```


## Instalación y ejecución

1. Clona o descarga el archivo 'Cifrado_Verman.py'
2. Abre una terminal en el directorio del archivo
3. Ejecuta el comando:
```bash
   python Cifrado_Verman.py
```


> [!NOTE]
> El alfabeto definido es más amplio que en el Vernam clásico (que suele usar solo letras), lo que permite cifrar mensajes con caracteres modernos.
> Se utiliza random.seed(time.time()) para asegurar la aleatoriedad en cada ejecución.


## Equipo 3

- Cruz Miranda Luis Eduardo
- De la rosa Lara Gustavo
- Domínguez Ríos Luis Daniel
- Hernández Hernández Deissy Jovita
- Mendoza Rodríguez Ángel Jesús
- Nieto Rodríguez Tomás Andrés
