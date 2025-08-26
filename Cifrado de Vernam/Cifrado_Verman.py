import random, time, os

abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789.,;:!?()[]{}<>@#$%^&*-_+=/\\|\"' "

N = len(abecedario)

def random_number():
    return random.randint(0, N - 1)

def charToInt(character):
    return abecedario.index(character)

def IntToChar(integer):
    return abecedario[integer]

def cifrar():
    mensaje = str(input("Escribe tu mensaje:\n> "))

    # Validar caracteres del mensaje
    for c in mensaje:
        if c not in abecedario:
            print(f"El caracter '{c}' no está en el abecedario definido.")
            return

    key_chars = []
    out_chars = []

    # Por cada carácter, elegimos una clave tal que (p ^ k) < N
    for c_m in mensaje:
        p = charToInt(c_m)
        while True:
            k = random_number()
            r = p ^ k           # XOR a nivel de bits
            if r < N:           # Solo aceptamos resultados que mapeen al abecedario
                key_chars.append(IntToChar(k))
                out_chars.append(IntToChar(r))
                break

    key = "".join(key_chars)
    resultado = "".join(out_chars)

    # Guardar en archivos
    with open("CM.txt", "w", encoding="utf-8") as f:
        f.write(resultado)

    with open("K.txt", "w", encoding="utf-8") as f:
        f.write(key)

    print("Key guardada en: K.txt")
    print("Mensaje cifrado guardado en: CM.txt")


def descifrar():
    print("=== Modo Descifrado ===")
    while True:
        ready = str(input("Tu mensaje cifrado está en CM.txt y la clave en K.txt. ¿Estás listo para descifrar? (s/n)\n> "))
        if ready.lower() == 's':
            try:
                with open("CM.txt", "r", encoding="utf-8") as f:
                    mensaje_cifrado = f.read()
                with open("K.txt", "r", encoding="utf-8") as f:
                    key = f.read()

                if len(mensaje_cifrado) != len(key):
                    print("Error: La longitud del mensaje cifrado y la clave no coinciden.")
                    return

                # p = c ^ k  (sin módulo)
                resultado = "".join(
                    IntToChar(charToInt(c_m) ^ charToInt(c_k))
                    for c_m, c_k in zip(mensaje_cifrado, key)
                )

                print(f"\nMensaje descifrado:\n{resultado}")

                # Eliminar los archivos después de descifrar
                os.remove("CM.txt")
                os.remove("K.txt")
                print("\nArchivos CM.txt y K.txt eliminados.")

            except FileNotFoundError:
                print("Error: No se encontraron los archivos CM.txt o K.txt.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")
            break
        elif ready.lower() == 'n':
            print("Regresando al menú...")
            break
        else:
            print("Por favor, responde con 's' o 'n'.")


# ----------------- MENÚ -----------------
random.seed(time.time())

while True:
    print("\n=== MENÚ ===")
    print("1. Cifrar mensaje")
    print("2. Descifrar mensaje")
    print("3. Salir")

    opcion = input("> ")

    if opcion == "1":
        cifrar()
    elif opcion == "2":
        descifrar()
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
