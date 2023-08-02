def es_palindromo(cadena):
    # Convertir la cadena a minúsculas para ignorar mayúsculas
    cadena = cadena.lower()
    # Eliminar los espacios en blanco de la cadena
    cadena = cadena.replace(" ", "")
    # Verificar si la cadena es igual a su reverso
    return cadena == cadena[::-1]

if __name__ == "__main__":
    texto = input("Ingresa una cadena de texto: ")

    if es_palindromo(texto):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")