alfabeto_minus = "abcdefghijklmnñopqrstuvwxyz"
alfabeto_mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def desplazar_caracter(caracter, corrimiento):
    # Minúsculas
    if caracter in alfabeto_minus:
        pos = alfabeto_minus.index(caracter)
        nueva_pos = (pos + corrimiento) % len(alfabeto_minus)
        return alfabeto_minus[nueva_pos]
    # Mayúsculas
    elif caracter in alfabeto_mayus:
        pos = alfabeto_mayus.index(caracter)
        nueva_pos = (pos + corrimiento) % len(alfabeto_mayus)
        return alfabeto_mayus[nueva_pos]
    # Cualquier otra cosa se queda igual
    else:
        return caracter

def cifrar(palabra, corrimiento):
    return "".join(desplazar_caracter(c, corrimiento) for c in palabra)

def decifrar(palabra, corrimiento):
    return "".join(desplazar_caracter(c, -corrimiento) for c in palabra)

while True:
    print("\n===== CIFRADO CESAR =====")
    palabra = input("Escribe la palabra o frase:\n> ")
    n = input("Elige:\n[1] Cifrar\n[2] Decifrar\n> ")
    if n not in ("1", "2"):
        print("Opción inválida.")
        continue

    try:
        c = int(input("Corrimiento (número entero):\n> "))
    except ValueError:
        print("Corrimiento inválido.")
        continue

    if n == "1":
        resultado = cifrar(palabra, c)
    else:
        resultado = decifrar(palabra, c)

    print(f"\nResultado: {resultado}")

    salir = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
    if salir == "n":
        print("Saliendo del programa...")
        break
