from collections import defaultdict, Counter
import re

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
    key = key.replace(" ", "")
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


def solo_letras(texto):
    return re.sub('[^A-Z]', '', texto.upper())

# Dividir ciphertext en columnas según longitud de clave
def dividir_columnas(ciphertext, key_len):
    columnas = [''] * key_len
    idx = 0
    for c in ciphertext:
        if c.isalpha():
            columnas[idx % key_len] += c.upper()
            idx += 1
    return columnas

def encontrar_repeticiones(texto, min_len=3, max_len=5):
    posiciones = defaultdict(list)
    N = len(texto)
    for L in range(min_len, max_len + 1):
        for i in range(N - L + 1):
            seq = texto[i:i+L]
            posiciones[seq].append(i)
    # filtrar las subcadenas que aparecen más de una vez
    return {s: pos for s, pos in posiciones.items() if len(pos) > 1}

def obtener_distancias(posiciones):
    distancias = []
    for pos_list in posiciones.values():
        pos_list = sorted(pos_list)
        for i in range(len(pos_list) - 1):
            distancias.append(pos_list[i+1] - pos_list[i])
    return distancias

def contar_divisores(distancias, max_div=30):
    contador = Counter()
    for d in distancias:
        for k in range(2, max_div + 1):
            if d % k == 0:
                contador[k] += 1
    return contador

def ranking_longitudes(contador):
    # ordenar solo por frecuencia de aparición (descendente)
    scored = [(k, v) for k, v in contador.items()]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored



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


    elif algoritmo == "2":
        print("\n===== ANALISIS DE KASISKI (solo tamaño de clave) =====")
        texto_cifrado = input("Escribe el texto cifrado:\n> ")
        texto = solo_letras(texto_cifrado)
        
        repeticiones = encontrar_repeticiones(texto, min_len=3, max_len=5)
        if not repeticiones:
            print("No se encontraron repeticiones suficientes.")
            continue
        
        distancias = obtener_distancias(repeticiones)
        contador = contar_divisores(distancias, max_div=30)
        ranking = ranking_longitudes(contador)
        
        print("\nTop longitudes candidatas:")
        for k, freq in ranking[:10]:
            print(f" - {k}: {freq} veces")



    salir = input("\n¿Quieres hacer otra operación? (s/n): ").lower()
    if salir == "n":
        print("Saliendo del programa...")
        break
