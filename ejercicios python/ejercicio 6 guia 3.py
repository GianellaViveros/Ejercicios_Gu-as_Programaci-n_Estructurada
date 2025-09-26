mejor_tiempo = 999999  
mejor_vehiculo = 0

for i in range(1,13):
    print("Competidor", i)

    numero = int(input("Número del vehículo: "))
    tiempo = float(input("Tiempo en segundos: "))

    if tiempo < mejor_tiempo:
        mejor_tiempo = tiempo
        mejor_vehiculo = numero

print("Carrera finalizada")
print("El vehículo", mejor_vehiculo)
print("Hizo el mejor tiempo:en ", mejor_tiempo)