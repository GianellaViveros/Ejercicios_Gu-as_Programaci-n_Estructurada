def comparar_edades(edad1, edad2):
    if edad1 > edad2:
        diferencia = edad1 - edad2
        return f"Hermano 1 es mayor por {diferencia} años."
    elif edad2 > edad1:
        diferencia = edad2 - edad1
        return f"Hermano 2 es mayor por {diferencia} años."
    else:
        return "Ambos hermanos tienen la misma edad."

print("Ingrese las edades de los dos hermanos:")
edad1 = int(input("Edad del Hermano 1: "))
edad2 = int(input("Edad del Hermano 2: "))

resultado = comparar_edades(edad1, edad2)
print(f"Resultado para las edades ingresadas: {resultado}")

escenarios = [
    (25, 29),
    (23, 18),
    (20, 20)
]

for i, (h1, h2) in enumerate(escenarios, start=1):
    resultado = comparar_edades(h1, h2)
    print(f"Escenario {i}: Hermano 1 = {h1}, Hermano 2 = {h2} → {resultado}")
