def inMatriz(c, matriz):
    return any(c in renglon for renglon in matriz)

def printMatrix(matriz):
    for renglon in matriz:
        for j in renglon:
            print("i/j  " if j == 'i' else f"{j}    ", end='')
        print()

def getRenglonColumna(c, matriz):
    cha = 'i' if c == 'j' else c
    for r, renglon in enumerate(matriz):
        for c, val in enumerate(renglon):
            if val == cha:
                return r, c
    return -1, -1

def getCaracter(i, j, matriz):
    return matriz[i][j]

def crearMatriz():
    abecedario = "abcdefghiklmnopqrstuvwxyz"
    matriz, renglon, columna = [], [], 0
    usados = set()

    # procesar llave
    for i in llave:
        c = 'i' if i == 'j' else i
        if c in usados:
            continue
        if columna > 4:
            matriz.append(renglon)
            renglon, columna = [], 0
        renglon.append(c)
        usados.add(c)
        columna += 1

    # completar con abecedario
    for i in abecedario:
        if i in usados:
            continue
        if columna > 4:
            matriz.append(renglon)
            renglon, columna = [], 0
        renglon.append(i)
        usados.add(i)
        columna += 1

    matriz.append(renglon)
    return matriz

def separador(mensaje):
    mensaje = mensaje.replace(" ", "")
    mensaje_separado = []
    if len(mensaje) % 2 == 1:
        mensaje += "x"
    for i in range(len(mensaje)):
        if i%2 == 1:
            mensaje_separado.append((mensaje[i-1], mensaje[i]))
    return mensaje_separado

def cifrado(mensaje_separado, matriz):
    mensaje_cifrado = ""

    for a, b in mensaje_separado:
        r1, c1 = getRenglonColumna(a, matriz)
        r2, c2 = getRenglonColumna(b, matriz)

        # Regla 1: misma columna → bajar
        if c1 == c2:
            r1, r2 = (r1 + 1) % 5, (r2 + 1) % 5
            mensaje_cifrado += getCaracter(r1, c1, matriz) + getCaracter(r2, c2, matriz)

        # Regla 2: mismo renglón → derecha
        elif r1 == r2:
            c1, c2 = (c1 + 1) % 5, (c2 + 1) % 5
            mensaje_cifrado += getCaracter(r1, c1, matriz) + getCaracter(r2, c2, matriz)

        # Regla 3: rectángulo → esquinas opuestas
        else:
            mensaje_cifrado += getCaracter(r1, c2, matriz) + getCaracter(r2, c1, matriz)

    return mensaje_cifrado

def descifrado(mensaje_separado, matriz):
    mensaje_descifrado = ""

    for a, b in mensaje_separado:
        r1, c1 = getRenglonColumna(a, matriz)
        r2, c2 = getRenglonColumna(b, matriz)

        # Regla 1: misma columna → subir
        if c1 == c2:
            r1, r2 = (r1 - 1) % 5, (r2 - 1) % 5
            mensaje_descifrado += getCaracter(r1, c1, matriz) + getCaracter(r2, c2, matriz)

        # Regla 2: mismo renglón → izquierda
        elif r1 == r2:
            c1, c2 = (c1 - 1) % 5, (c2 - 1) % 5
            mensaje_descifrado += getCaracter(r1, c1, matriz) + getCaracter(r2, c2, matriz)

        # Regla 3: rectángulo → esquinas opuestas (igual que en cifrado)
        else:
            mensaje_descifrado += getCaracter(r1, c2, matriz) + getCaracter(r2, c1, matriz)

    return mensaje_descifrado


while True:
    print("========= CIFRADO WHEATSTONE =========")
    # llave = input("Ingresa tu llave\n> ").lower().replace(" ", "")
    llave = "panconjamon" # llave rápida para pruebas
    print(f"Tu tabla con tu llave [{llave}]:")
    tablaCifrado = crearMatriz()
    printMatrix(tablaCifrado)

    mensaje = input("\nIngresa tu mensaje\n> ").lower().replace(" ", "")

    print("\n¿Qué deseas hacer?")
    print("[1] Cifrar")
    print("[2] Descifrar")
    opcion = input("> ")

    if opcion == "1":
        mensaje_cifrado = cifrado(separador(mensaje), tablaCifrado)
        print(f"\n🔐 Mensaje cifrado:\n> {mensaje_cifrado}")

    elif opcion == "2":
        mensaje_descifrado = descifrado(separador(mensaje), tablaCifrado)
        print(f"\n🔓 Mensaje descifrado:\n> {mensaje_descifrado}")

    else:
        print("\nOpción no válida.")


    if input("¿Desea continuar? s/n\n> ").lower() == 'n':
        break





