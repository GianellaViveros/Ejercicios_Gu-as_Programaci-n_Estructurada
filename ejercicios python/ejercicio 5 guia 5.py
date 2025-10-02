matriz = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    print(f"Ingresar notas para el alumno {i + 1}:")
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Nota {j + 1}: "))
                if 0 < nota <= 10: 
                    matriz[i][j] = nota
                    break
                else:
                    print("Error: La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Error: Ingrese un número válido.")

for i in range(4):
    promedio = sum(matriz[i][0:3]) / 3
    matriz[i][3] = promedio

print("Notas y promedio de cada alumno:")
print(f"{'Alumno':<10}{'Nota 1':<8}{'Nota 2':<8}{'Nota 3':<8}{'Promedio':<8}")
for i in range(4):
    print(f"{i+1:<10}{matriz[i][0]:<8}{matriz[i][1]:<8}{matriz[i][2]:<8}{matriz[i][3]:.2f}")