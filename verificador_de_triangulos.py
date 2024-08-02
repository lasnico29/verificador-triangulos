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

        # Verificar que ninguno de los lados sea cero
        if a == 0 or b == 0 or c == 0:
            
            print("Error: Los lados de un triángulo no pueden ser cero. Por favor, ingrese valores válidos.")
            continue

        tipo = determinar_tipo_triangulo(a, b, c)
        print(f"El triángulo es {tipo}.")

        otra_vez = input("¿Quieres analizar otro triángulo? (s/n): ").lower()
        if otra_vez != 's':
            print("Gracias por usar el programa. ¡Adiós!")
            break


if __name__ == "__main__":
    main()
