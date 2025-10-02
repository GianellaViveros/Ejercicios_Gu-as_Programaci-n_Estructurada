n = int(input("¿Cuántas notas son? "))

if n <= 0:
    print("La cantidad de notas tiene ue ser mayor a 0. ")
else:
    notas = []

    for i in range(n):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)

    nota_max = max(notas)
    promedio = sum(notas)/n

    print("Notas ingresadas", notas)
    print("Nota más alta", nota_max)
    print("El promedio es: ", round(promedio,2))