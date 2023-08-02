def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

if __name__ == "__main__":
    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))

    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")