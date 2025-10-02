Edades = []

for i in range(20):
    edad = (int(input(f"Ingrese edad de la persona {i + 1}:")))
    Edades.append(edad)

promedio = sum(Edades)/ len(Edades)
edad_minima = min(Edades)

print("Promedio de edad: ", round(promedio,2))
print("Edad de la persona más joven: ", edad_minima)