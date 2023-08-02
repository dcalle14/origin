def encontrar_max_y_min(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

if __name__ == "__main__":
    lista_dada = [10, 5, 20, 8, 15]  # Puedes ajustar la lista aquí con los números que desees

    maximo_numero, minimo_numero = encontrar_max_y_min(lista_dada)
    print(f"El número más grande en la lista es: {maximo_numero}")
    print(f"El número más pequeño en la lista es: {minimo_numero}")