# Definimos la matriz 3x3
matriz = [
    [5, 8, 12],
    [9, 3, 7],
    [4, 6, 1]
]

def buscar_valor(matriz, valor_buscado):
    # Recorremos la matriz para encontrar el valor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                # Si se encuentra el valor, se devuelve su posición
                return i, j
    # Si no se encuentra el valor, se devuelve None
    return None

# Valor que queremos buscar
valor_a_buscar = 7

# Llamada a la función para buscar el valor
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"Valor {valor_a_buscar} encontrado en la posición {posicion}")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz")