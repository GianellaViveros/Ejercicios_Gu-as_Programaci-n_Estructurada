sueldos = []

for i in range (10):
    sueldo = float(input(f"Ingrese el sueldo del empleado {i + 1}:"))
    sueldos.append(sueldo)

print("Sueldos")
for i in range (10):
    print(f"Empleado {i + 1}: ${sueldos[i]}")

mayor_sueldo = max(sueldos)

print("El mayor sueldo es: $", mayor_sueldo)