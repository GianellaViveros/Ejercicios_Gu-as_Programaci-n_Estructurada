n = int(input("¿Cuántas notas son?: "))

notas = []
aprobados = 0
desaprobados = 0

for i in range(n):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print("Notas ingresadas: ", notas)
print("Cantidad de aprobados: ", aprobados)
print("Cantidad de desaprobados: ", desaprobados)