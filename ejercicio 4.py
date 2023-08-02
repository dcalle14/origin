def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

if __name__ == "__main__":
    numero_dado = int(input("Ingresa un número: "))

    resultado = es_par_o_impar(numero_dado)
    print(f"El número {numero_dado} es {resultado}.")