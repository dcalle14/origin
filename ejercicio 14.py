def calcular_media_aritmetica(lista):
    if not lista:
        return 0
    suma = sum(lista)
    media = suma / len(lista)
    return media

if __name__ == "__main__":
    lista_numeros = [10, 20, 30, 40, 50]

    media_aritmetica = calcular_media_aritmetica(lista_numeros)
    print(f"La media aritmética de la lista es: {media_aritmetica:.2f}")