notas = []

for i in range(40):
    print(f"Alumno {i + 1}:")
    fila_notas = []
    
    for j in range(5):
        nota = float(input(f"Ingrese la nota {j + 1}: "))
        fila_notas.append(nota)
    
    notas.append(fila_notas)

print("Promedio de cada alumno")
for i in range(40):
    promedio = sum(notas[i]) / 5
    print(f"Alumno {i + 1} → Promedio: {promedio:.2f}")