if __name__ == "__main__":
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2

        if num2 == 0:
            division = "No es posible dividir entre cero."
        else:
            division = num1 / num2

        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        print(f"División: {division}")

    except ValueError:
        print("Error: Ingresa dos números válidos.")