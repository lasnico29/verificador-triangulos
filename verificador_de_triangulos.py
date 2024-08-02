def determinar_tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    while True:
        print("Ingrese los lados del triángulo:")
        a = float(input("Lado A: "))
        b = float(input("Lado B: "))
        c = float(input("Lado C: "))

        tipo = determinar_tipo_triangulo(a, b, c)
        print(f"El triángulo es {tipo}.")

        otra_vez = input("¿Quieres analizar otro triángulo? (s/n): ").lower()
        if otra_vez != 's':
            print("Gracias por usar el programa. ¡Adiós!")
            break

if __name__ == "__main__":
    main()
