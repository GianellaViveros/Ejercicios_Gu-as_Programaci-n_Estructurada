def tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Triángulo Equilátero"
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        return "Triángulo Escaleno"
    else:
        return "Triángulo Isósceles"


lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    resultado = tipo_triangulo(lado1, lado2, lado3)
    print(f"El triángulo con lados {lado1}, {lado2}, {lado3} es: {resultado}")
else:
    print("Los lados ingresados no forman un triángulo válido.")


print("Prueba de escenarios")
escenarios = [
    (10, 15, 20),
    (30, 30, 30),
    (20, 20, 30)
]

for i, (l1, l2, l3) in enumerate(escenarios, start=1):
    resultado = tipo_triangulo(l1, l2, l3)
    print(f"Escenario {i}: Lados = {l1}, {l2}, {l3} → {resultado}")