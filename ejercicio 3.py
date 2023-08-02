import random

def generar_lista_aleatoria(longitud, rango_min, rango_max):
    lista_aleatoria = [random.randint(rango_min, rango_max) for _ in range(longitud)]
    return lista_aleatoria

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

if __name__ == "__main__":
    longitud_lista = 10
    valor_minimo = 1
    valor_maximo = 100

    lista_aleatoria = generar_lista_aleatoria(longitud_lista, valor_minimo, valor_maximo)
    imprimir_lista(lista_aleatoria)