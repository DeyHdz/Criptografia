#Cifrado de Hill
import random
import time

abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N = len(abecedario)

def random_number():
    return random.randint(0, N - 1)

def create_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random_number())
        matrix.append(row)
    return matrix

# This function returns the transpose of a matrix
def transposeMatrix(m):
    transpose=list(map(list,zip(*m)))
    #print('transpose of cofactor matrix->',transpose)
    return transpose

# This function returns the minor matrix of the element
# at postion i,j
def getMatrixMinor(m,i,j):
    minor_matrix = [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
    return minor_matrix

# This function find the determinant of the matrix
def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    #print('determinant=',determinant)
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if(determinant==0):
        print('Error! Determinant of the matrix is zero')
        print('Inverse cannot be calculated')
        return
    
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
        
    # Transposing the cofactor matrix to get disjoint
    Disjoint = transposeMatrix(cofactors)
    
    # Dividing each element of the adjoint matrix by the determinant
    for r in range(len(Disjoint)):
        for c in range(len(Disjoint)):
            Disjoint[r][c] = Disjoint[r][c]/determinant
            
    return Disjoint

def constant_matrix_mult(matrix, constant):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = (matrix[i][j] * constant) % N
    return matrix

def mod_inverse(a, m):
    """Calcula el inverso modular de a mod m usando Euclides extendido"""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # no existe inverso
        

def inverse_matrix(m):
    n = len(m)
    det = getMatrixDeternminant(m) % N
    inv_det = mod_inverse(det, N)
    if inv_det is None:
        raise ValueError(f"La matriz no es invertible mod {N}")

    # matriz de cofactores
    cofactors = []
    for r in range(n):
        cofactor_row = []
        for c in range(n):
            minor = getMatrixMinor(m, r, c)
            cofactor_row.append(((-1) ** (r + c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactor_row)

    # adjunta = transpuesta de cofactores
    adjugate = transposeMatrix(cofactors)

    # inversa = adjugate * inv_det mod N
    for r in range(n):
        for c in range(n):
            adjugate[r][c] = (adjugate[r][c] * inv_det) % N

    return adjugate

def multiply_matrix_vector(matrix, vector):
    """Multiplica matriz (n x n) por vector (n x 1) módulo N"""
    n = len(matrix)
    result = [0] * n
    for i in range(n):
        for j in range(n):
            result[i] += matrix[i][j] * vector[j]
        result[i] %= N
    return result

def hill_encrypt(text, key):
    """Cifra el texto con la clave (matriz)"""
    text = text.upper().replace(" ", "")
    n = len(key)

    # convertir letras a números
    nums = [index_letra(c) for c in text]

    # padding con 'X'
    while len(nums) % n != 0:
        nums.append(index_letra("X"))

    # dividir en bloques y cifrar
    encrypted_nums = []
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        encrypted_block = multiply_matrix_vector(key, block)
        encrypted_nums.extend(encrypted_block)

    return "".join(letra_index(num) for num in encrypted_nums)


def hill_decrypt(ciphertext, key):
    """Descifra el texto con la clave (matriz)"""
    n = len(key)
    inv_key = inverse_matrix(key)
    print("Matriz inversa:")
    print_matrix(inv_key)

    nums = [index_letra(c) for c in ciphertext]
    decrypted_nums = []
    for i in range(0, len(nums), n):
        block = nums[i:i+n]
        decrypted_block = multiply_matrix_vector(inv_key, block)
        decrypted_nums.extend(decrypted_block)

    return "".join(letra_index(num) for num in decrypted_nums)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{num:2}" for num in row), end="\n")

def index_letra(letra):
    return abecedario.index(letra)

def letra_index(index):
    return abecedario[index]


while True:
    print("================Cifrado de Hill================")
    print("1. Cifrar/Descifrar")
    print("2. Salir")

    opcion = input("Selecciona una opción: \n> ")

    if opcion == "2":
        print("Saliendo...")
        break
    elif opcion == "1":
        print("Cifrado de Hill seleccionado.")
        
        # Pedir palabra
        mensaje = input("Ingresa una palabra a cifrar: ")
        longitud = len(mensaje)

        # Intentar generar matriz válida desde tamaño completo hacia atrás
        for n in range(longitud, 1, -1):  # n, n-1, ..., 2
            start_time = time.time()
            found = False
            while True:
                key = create_matrix(n)
                det = getMatrixDeternminant(key) % N
                if det != 0 and gcd(det, N) == 1:
                    found = True
                    break

                # Si tarda más de 1 segundo intentando, salir y probar tamaño menor
                if time.time() - start_time > 1.0:
                    break

            if found:
                print(f"Matriz clave válida de tamaño {n} encontrada:")
                print_matrix(key)
                break
        else:
            raise ValueError("No se pudo generar ninguna matriz válida.")

        # Ajustar mensaje para múltiplos de n
        nums = [index_letra(c) for c in mensaje.upper() if c.isalpha()]
        while len(nums) % n != 0:
            nums.append(index_letra("X"))

        mensaje_ajustado = "".join(letra_index(num) for num in nums)

        # Cifrado y descifrado
        cifrado = hill_encrypt(mensaje_ajustado, key)
        descifrado = hill_decrypt(cifrado, key)

        print("Texto original :", mensaje_ajustado)
        print("Texto cifrado  :", cifrado)
        print("Texto descifrado:", descifrado)

    else:
        print("Opción no válida. Intenta de nuevo.")