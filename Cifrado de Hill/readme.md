# Cifrado de Hill

## Descripción

Este proyecto implementa el **Cifrado de Hill**, un algoritmo de criptografía clásica que utiliza álgebra lineal para cifrar y descifrar mensajes. El cifrado emplea matrices cuadradas como claves criptográficas y opera sobre bloques de texto, transformándolos mediante operaciones matriciales en aritmética modular.

El programa genera automáticamente matrices clave válidas (invertibles) y permite cifrar y descifrar mensajes de manera interactiva, adaptándose dinámicamente al tamaño del texto de entrada.

## Características

- ✅ **Generación automática de matrices clave**: Crea matrices invertibles válidas para el cifrado
- ✅ **Adaptabilidad dinámica**: Ajusta el tamaño de la matriz según la longitud del mensaje
- ✅ **Validación matemática**: Verifica que las matrices sean invertibles en módulo 26
- ✅ **Padding automático**: Completa mensajes con 'X' para ajustar a bloques completos
- ✅ **Interfaz interactiva**: Menu de opciones fácil de usar
- ✅ **Soporte completo del alfabeto**: Trabaja con las 26 letras del alfabeto inglés
- ✅ **Optimización temporal**: Sistema de timeout para evitar búsquedas infinitas de matrices

## Cómo Funciona

### Proceso de Cifrado
1. **Preparación del texto**: Se convierte a mayúsculas y se eliminan espacios
2. **Generación de matriz clave**: Se busca una matriz cuadrada invertible en módulo 26
3. **División en bloques**: El texto se divide en bloques del tamaño de la matriz
4. **Cifrado por bloques**: Cada bloque se multiplica por la matriz clave
5. **Conversión final**: Los números resultantes se convierten de vuelta a letras

### Proceso de Descifrado
1. **Cálculo de matriz inversa**: Se obtiene la inversa de la matriz clave en módulo 26
2. **División del texto cifrado**: Se separa en bloques del mismo tamaño
3. **Descifrado por bloques**: Cada bloque se multiplica por la matriz inversa
4. **Reconstrucción**: Se obtiene el mensaje original

## Estructura del Código

```
cifrado_hill.py
├── Variables globales
│   ├── abecedario (A-Z)
│   └── N = 26
├── Funciones de matrices
│   ├── create_matrix()
│   ├── transposeMatrix()
│   ├── getMatrixMinor()
│   ├── getMatrixDeternminant()
│   └── inverse_matrix()
├── Funciones de cifrado
│   ├── hill_encrypt()
│   ├── hill_decrypt()
│   └── multiply_matrix_vector()
├── Funciones auxiliares
│   ├── mod_inverse()
│   ├── gcd()
│   ├── index_letra()
│   └── letra_index()
└── Programa principal
    └── Menú interactivo
```

## Funciones Principales

### `create_matrix(size)`
Genera una matriz cuadrada de números aleatorios entre 0 y 25.

### `inverse_matrix(m)`
Calcula la matriz inversa en módulo 26 utilizando:
- Determinante de la matriz
- Matriz de cofactores
- Matriz adjunta (transpuesta de cofactores)
- Inverso modular del determinante

### `hill_encrypt(text, key)`
Cifra el texto usando la matriz clave:
- Convierte letras a números (A=0, B=1, ..., Z=25)
- Aplica padding si es necesario
- Multiplica cada bloque por la matriz clave

### `hill_decrypt(ciphertext, key)`
Descifra el texto usando la matriz inversa de la clave.

### `mod_inverse(a, m)`
Encuentra el inverso modular de un número usando el algoritmo de Euclides extendido.

## Ejemplo de Uso

```
================Cifrado de Hill================
1. Cifrar/Descifrar
2. Salir
Selecciona una opción: 
> 1

Ingresa una palabra a cifrar: HOLA

Matriz clave válida de tamaño 2 encontrada:
 3 15
 8 21

Matriz inversa:
 9  1
18  7

Texto original : HOLAX
Texto cifrado  : KQWPX
Texto descifrado: HOLAX
```

## Instalación y Ejecución

### Requisitos
- Python 3.6 o superior
- No se requieren librerías externas (solo módulos estándar: `random`, `time`)

### Instalación
```bash
# Clonar o descargar el archivo
git clone [URL_del_repositorio]
# o descargar cifrado_hill.py directamente
```

### Ejecución
```bash
# Ejecutar el programa
python cifrado_hill.py

# o en algunos sistemas
python3 cifrado_hill.py
```

### Instrucciones de Uso
1. Ejecuta el programa
2. Selecciona la opción "1" para cifrar/descifrar
3. Ingresa el texto que deseas cifrar
4. El programa generará automáticamente una matriz clave válida
5. Mostrará el texto original, cifrado y descifrado

## Consideraciones Técnicas

- **Aritmética Modular**: Todas las operaciones se realizan en módulo 26
- **Matrices Invertibles**: Solo se utilizan matrices con determinante coprimo con 26
- **Optimización**: Sistema de timeout para evitar búsquedas excesivamente largas
- **Padding**: Se añade 'X' automáticamente para completar bloques

## Limitaciones

- Solo funciona con el alfabeto inglés (A-Z)
- No preserva espacios ni caracteres especiales
- El tamaño de la matriz está limitado por la longitud del mensaje
- Vulnerable a ataques de frecuencia en textos largos

---

## Equipo 3

**Integrantes:**
- Cruz Miranda Luis Eduardo
- De la rosa Lara Gustavo  
- Domínguez Ríos Luis Daniel
- Hernández Hernández Deissy Jovita
- Mendoza Rodríguez Ángel Jesús
- Nieto Rodríguez Tomás Andrés

---

*Proyecto desarrollado como parte del curso de Criptografía - Implementación del Cifrado de Hill en Python*
