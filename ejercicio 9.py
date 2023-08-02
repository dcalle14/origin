def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            # Puedes modificar la forma en que se generan los números en la matriz
            fila.append(i * columnas + j + 1)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

if __name__ == "__main__":
    filas_matriz = 3  # Puedes ajustar la cantidad de filas de la matriz aquí
    columnas_matriz = 4  # Puedes ajustar la cantidad de columnas de la matriz aquí

    matriz_generada = generar_matriz(filas_matriz, columnas_matriz)
    imprimir_matriz(matriz_generada)