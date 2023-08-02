def calcular_suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

if __name__ == "__main__":
    lista_dada = [1, 2, 3, 4, 5]  # Puedes ajustar la lista aquí con los números que desees

    suma_total = calcular_suma_lista(lista_dada)
    print(f"La suma de los números en la lista es: {suma_total}")