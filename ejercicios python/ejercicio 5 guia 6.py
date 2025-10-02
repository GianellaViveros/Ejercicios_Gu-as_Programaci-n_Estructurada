def ordenar_dos_numeros(a, b):
    if a < b:
        return a, b
    else:
        return b, a

print("Ingrese dos números:")
a = float(input("Ingrese el número a: "))
b = float(input("Ingrese el número b: "))

menor, mayor = ordenar_dos_numeros(a, b)
print(f"Números ordenados: {menor}, {mayor}")

# Prueba de escritorio con escenarios dados
escenarios = [(5, 9), (8, 3)]
print("Prueba de escritorio con escenarios dados:")
for a, b in escenarios:
    menor, mayor = ordenar_dos_numeros(a, b)
    print(f"Entrada: a={a}, b={b} → Ordenados: {menor}, {mayor}")
