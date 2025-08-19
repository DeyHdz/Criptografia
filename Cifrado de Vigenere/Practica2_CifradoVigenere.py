alfabeto_minus = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

def ajustar_llave(key, mensaje):
    espacios = 0
    key = key.upper()
    key_nueva = ""
    if len(key) == len(mensaje):
        return key
    for i in range(len(mensaje)):
        if(mensaje[i] == " "):
            key_nueva += " "
            espacios += 1
            continue
        key_nueva += key[(i-espacios) % len(key)]
    return key_nueva


while True:
    print("\n=======================")
    print("===== PRACTICA 02 =====")
    print("=======================")
    algoritmo = str(input("\n[1] Algoritmo Criptografico\n[2] Algoritmo Criptoanalisis\n> "))
    if algoritmo not in ("1", "2"):
        print("Opción inválida.")
        continue
    elif algoritmo == "1":
        '''
        En esta parte va todo lo del algoritmo de Vigenère
        Se incluye la opción de Cifrar y Decifrar
        Se ingresa un mensaje tipo cadena de tamaño n
        Se ingresa una llave tipo cadena ABC de tamaño m
        '''        
        print("\n===== CIFRADO DE VEGENERE =====")
        palabra = input("Escribe la palabra o frase:\n> ")
        n = input("Elige:\n[1] Cifrar\n[2] Decifrar\n> ")
        key_original = str(input("Ingresa tu llave \n> "))

        key_ajustada = ajustar_llave(key_original, palabra)
        print(key_ajustada)

        if n not in ("1", "2"):
            print("Opción inválida.")
            continue

        resultado = ""
        if n == "1":
            for i in range(len(palabra)):
                resultado += cifrar(palabra[i],ord(key_ajustada[i])-65)
        else:
            for i in range(len(palabra)):
                resultado += decifrar(palabra[i],ord(key_ajustada[i])-65)

        print(f"\nResultado: {resultado}")


    else:
        
        '''
        Aqui va la Parte de Kasiski




        '''
        pass


    salir = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
    if salir == "n":
        print("Saliendo del programa...")
        break
