# Algoritmo de Euclides Extendido

## Descripción

Este proyecto implementa el **Algoritmo de Euclides Extendido**, una extensión del clásico algoritmo de Euclides que no solo calcula el máximo común divisor (MCD) de dos números enteros, sino que también encuentra los coeficientes de la **Identidad de Bézout**. Esta identidad establece que para cualquier par de enteros `a` y `b`, existen enteros `x` e `y` tales que: **ax + by = mcd(a,b)**.

El programa proporciona una interfaz interactiva que permite calcular el MCD y los coeficientes de Bézout para cualquier par de números enteros no negativos, con verificación automática de los resultados.

## Características

- ✅ **Cálculo eficiente del MCD**: Implementación recursiva del algoritmo de Euclides
- ✅ **Coeficientes de Bézout**: Encuentra los valores x e y de la identidad de Bézout
- ✅ **Verificación automática**: Comprueba que ax + by = mcd(a,b)
- ✅ **Interfaz interactiva**: Permite múltiples cálculos en una sola ejecución
- ✅ **Validación de entrada**: Manejo de errores y validación de datos
- ✅ **Casos base optimizados**: Maneja correctamente los casos límite
- ✅ **Salida detallada**: Muestra todos los resultados de forma clara y organizada

## Cómo Funciona

### Fundamento Matemático
El algoritmo se basa en la **Identidad de Bézout**, que establece que para enteros `a` y `b`:
```
ax + by = mcd(a, b)
```

### Proceso del Algoritmo
1. **Caso base**: Si `a = 0`, entonces `mcd(0, b) = b` con coeficientes `x = 0, y = 1`
2. **Recursión**: Para `a ≠ 0`, se aplica recursivamente con `(b mod a, a)`
3. **Retropropagación**: Los coeficientes se actualizan usando las relaciones:
   - `x = y₁ - (b ÷ a) × x₁`
   - `y = x₁`
4. **Verificación**: Se comprueba que `ax + by = mcd(a,b)`

### Complejidad
- **Temporal**: O(log(min(a,b))) - misma que el algoritmo de Euclides clásico
- **Espacial**: O(log(min(a,b))) - debido a la pila de recursión

## Estructura del Código

```
euclides_extendido.py
├── Función principal
│   └── algoritmo_euclides_extendido(a, b)
│       ├── Caso base (a == 0)
│       ├── Llamada recursiva
│       └── Actualización de coeficientes
└── Programa interactivo
    ├── Entrada de datos
    ├── Validación de entrada
    ├── Llamada al algoritmo
    ├── Mostrar resultados
    ├── Verificación de Bézout
    └── Control de flujo (continuar/salir)
```

## Funciones Principales

### `algoritmo_euclides_extendido(a, b)`

**Parámetros:**
- `a`: Primer número entero no negativo
- `b`: Segundo número entero no negativo

**Retorna:**
- `mcd`: Máximo común divisor de a y b
- `x`: Coeficiente x de la identidad de Bézout
- `y`: Coeficiente y de la identidad de Bézout

**Funcionamiento:**
1. **Caso base**: Si a = 0, retorna (b, 0, 1)
2. **Recursión**: Calcula `algoritmo_euclides_extendido(b % a, a)`
3. **Actualización**: Calcula los nuevos coeficientes usando las fórmulas de retropropagación

### Programa Principal

**Características:**
- Bucle interactivo para múltiples cálculos
- Validación de entrada con manejo de excepciones
- Verificación automática de la identidad de Bézout
- Opción de continuar o salir del programa

## Ejemplo de Uso

```
--- Cálculo del MCD y coeficientes de Bézout ---
Ingrese el primer número (a): 35
Ingrese el segundo número (b): 15

El máximo común divisor de 35 y 15 es: 5
Los coeficientes x e y son: x = 1, y = -2
Verificación de la identidad de Bézout: 35*(1) + 15*(-2) = 5

¿Desea calcular otro MCD? (s/n): s

--- Cálculo del MCD y coeficientes de Bézout ---
Ingrese el primer número (a): 48
Ingrese el segundo número (b): 18

El máximo común divisor de 48 y 18 es: 6
Los coeficientes x e y son: x = -1, y = 3
Verificación de la identidad de Bézout: 48*(-1) + 18*(3) = 6

¿Desea calcular otro MCD? (s/n): n
```

## Instalación y Ejecución

### Requisitos
- Python 3.6 o superior
- No se requieren librerías externas (solo funciones built-in de Python)

### Instalación
```bash
# Clonar o descargar el archivo
git clone [URL_del_repositorio]
# o descargar euclides_extendido.py directamente
```

### Ejecución
```bash
# Ejecutar el programa
python euclides_extendido.py

# o en algunos sistemas
python3 euclides_extendido.py
```

### Instrucciones de Uso
1. Ejecuta el programa
2. Ingresa el primer número (a) cuando se solicite
3. Ingresa el segundo número (b) cuando se solicite
4. Observa los resultados: MCD y coeficientes de Bézout
5. Verifica que la identidad de Bézout se cumple
6. Decide si deseas realizar otro cálculo o salir

## Casos de Prueba

### Casos Típicos
```
Entrada: a=35, b=15
Salida: mcd=5, x=1, y=-2
Verificación: 35(1) + 15(-2) = 35 - 30 = 5 ✓

Entrada: a=48, b=18
Salida: mcd=6, x=-1, y=3
Verificación: 48(-1) + 18(3) = -48 + 54 = 6 ✓
```

### Casos Especiales
```
Entrada: a=0, b=5
Salida: mcd=5, x=0, y=1
Verificación: 0(0) + 5(1) = 5 ✓

Entrada: a=7, b=0
Salida: mcd=7, x=1, y=0
Verificación: 7(1) + 0(0) = 7 ✓
```

## Aplicaciones Prácticas

### Criptografía
- Cálculo de inversos modulares para algoritmos como RSA
- Implementación de operaciones en cuerpos finitos

### Teoría de Números
- Resolución de ecuaciones diofánticas lineales
- Cálculo de fracciones en forma reducida

### Álgebra Computacional
- Operaciones con polinomios
- Sistemas de ecuaciones modulares

## Consideraciones Técnicas

- **Recursión**: El algoritmo utiliza recursión, limitada por la profundidad de la pila
- **Eficiencia**: Complejidad logarítmica, muy eficiente incluso para números grandes
- **Precisión**: Trabaja con aritmética entera exacta, sin errores de punto flotante
- **Validación**: Incluye verificación automática de resultados

## Limitaciones

- Solo acepta números enteros no negativos como entrada
- La recursión puede causar stack overflow para números extremadamente grandes
- No optimizado para operaciones con números de precisión arbitraria
- La interfaz de usuario es básica (línea de comandos)

## Fundamento Teórico

### Identidad de Bézout
Para cualquier par de enteros a y b, existen enteros x e y tales que:
```
ax + by = mcd(a, b)
```

### Relaciones de Recurrencia
Si `mcd, x₁, y₁ = euclides_extendido(b mod a, a)`, entonces:
```
x = y₁ - (b ÷ a) × x₁
y = x₁
```

### Propiedades
- Los coeficientes x e y no son únicos
- Si (x₀, y₀) es una solución, entonces todas las soluciones son de la forma:
  ```
  x = x₀ + k(b/mcd)
  y = y₀ - k(a/mcd)
  ```
  donde k es cualquier entero.

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

*Proyecto desarrollado como parte del curso de Criptografía - Implementación del Algoritmo de Euclides Extendido en Python*
