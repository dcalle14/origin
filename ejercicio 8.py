def invertir_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

if __name__ == "__main__":
    lista_dada = [1, 2, 3, 4, 5]  # Puedes ajustar la lista aquí con los elementos que desees

    lista_invertida = invertir_lista(lista_dada)
    print(f"Lista original: {lista_dada}")
    print(f"Lista invertida: {lista_invertida}")