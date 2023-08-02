def factorial(numero):
    if numero < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

if __name__ == "__main__":
    numero_dado = int(input("Ingresa un número entero no negativo: "))

    try:
        resultado_factorial = factorial(numero_dado)
        print(f"El factorial de {numero_dado} es {resultado_factorial}.")
    except ValueError as e:
        print(e)