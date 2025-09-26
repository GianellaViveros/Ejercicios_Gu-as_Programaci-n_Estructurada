tenis = 0
futbol = 0

# [cantidad, suma_edades]
edad_por_deporte = {
    1: [0, 0],  # Tenis
    2: [0, 0],  # Rugby
    3: [0, 0],  # Voley
    4: [0, 0],  # Hockey
    5: [0, 0]   # Fútbol
}

cantidad = int(input("¿Cuántos socios?: "))

for i in range(cantidad):
    print(i + 1)
    numero = int(input("Número de socio: "))
    edad = int(input("Edad: "))
    print("Deporte: 1-Tenis  2-Rugby  3-Voley  4-Hockey  5-Fútbol")
    deporte = int(input("Ingrese el número del deporte: "))

    if deporte == 1:
        tenis += 1
    elif deporte == 5:
        futbol += 1

    # cantidad y suma de edades por deporte
    if deporte in edad_por_deporte:
        edad_por_deporte[deporte][0] += 1  # cantidad
        edad_por_deporte[deporte][1] += edad  # suma de edades
    else:
        print("Deporte inválido.")

print("Socios que practican Tenis:", tenis)
print(f"Socios que practican Fútbol:", futbol)

nombres = ["", "Tenis", "Rugby", "Voley", "Hockey", "Fútbol"]

for i in range(1, 6):
    cant = edad_por_deporte[i][0]
    suma = edad_por_deporte[i][1]
    if cant > 0:
        promedio = suma / cant
        print("Promedio de edad: ", promedio)
    else:
        print("No hay socios que practiquen")