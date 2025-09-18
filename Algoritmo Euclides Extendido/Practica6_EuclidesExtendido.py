def algoritmo_euclides_extendido(a, b):
    """
    Calcula el máximo común divisor (MCD) de a y b,
    y encuentra los coeficientes x e y que satisfacen la identidad de Bézout.

    Retorna una tupla (mcd, x, y).
    """
    # Casos base de la recursión
    if a == 0:
        return b, 0, 1

    # Llamada recursiva
    mcd, x1, y1 = algoritmo_euclides_extendido(b % a, a)

    # Actualización de resultados usando los valores de la llamada recursiva
    x = y1 - (b // a) * x1
    y = x1

    return mcd, x, y


while True:
    print("\n--- Cálculo del MCD y coeficientes de Bézout ---")
    try:
        a = int(input("Ingrese el primer número (a): "))
        b = int(input("Ingrese el segundo número (b): "))
        
        if a < 0 or b < 0:
            print("Por favor, ingrese números enteros no negativos.")
            continue

        mcd, x, y = algoritmo_euclides_extendido(a, b)

        print(f"\nEl máximo común divisor de {a} y {b} es: {mcd}")
        print(f"Los coeficientes x e y son: x = {x}, y = {y}")
        print(f"Verificación de la identidad de Bézout: {a}*({x}) + {b}*({y}) = {a*x + b*y}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")


    continuar = input("\n¿Desea calcular otro MCD? (s/n): ").strip().lower()
    if continuar != 's':
        break
# --- Fin del código ---