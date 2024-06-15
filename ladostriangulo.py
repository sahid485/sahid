import math

def calcular_lado_faltante():
    print("Ingresa los valores de los lados:")
    Lado1 = input("Lado 1 (Cateto Adyacente): ")
    Lado2 = input("Lado 2 (Cateto Opuesto): ")
    Lado3 = input("Lado 3 (Hipotenusa): ")

    Lado1 = float(Lado1) if Lado1 else 0
    Lado2 = float(Lado2) if Lado2 else 0
    Lado3 = float(Lado3) if Lado3 else 0

    if Lado3 == 0:
        Lado3 = math.sqrt(Lado1**2 + Lado2**2)
        lado_calculado = "hipotenusa"
    elif Lado1 == 0:
        Lado1 = math.sqrt(Lado3**2 - Lado2**2)
        lado_calculado = "cateto adyacente"
    elif Lado2 == 0:
        Lado2 = math.sqrt(Lado3**2 - Lado1**2)
        lado_calculado = "cateto opuesto"
    else:
        print("Error: No se puede calcular el lado faltante.")
        return

    print(f"El lado faltante ({lado_calculado}) es: {Lado3 if lado_calculado == 'hipotenusa' else (Lado1 if lado_calculado == 'cateto adyacente' else Lado2)}")

calcular_lado_faltante()
