def es_bisiesto(año):  
    if (año % 400 == 0):
        return True
    elif (año % 100 == 0):
        return False
    elif (año % 4 == 0):
        return True
    else:
        return False

año_usuario = int(input("Ingrese un año para verificar si es bisiesto: "))

if es_bisiesto(año_usuario):
    print(f"El año {año_usuario} es bisiesto.")
else:
    print(f"El año {año_usuario} no es bisiesto.")

print("Prueba con los siguientes escenarios:")
escenarios = [
    2000, 
    1900
    ]

for año in escenarios:
    resultado = "bisiesto" if es_bisiesto(año) else "no bisiesto"
    print(f"Año {año}: {resultado}")