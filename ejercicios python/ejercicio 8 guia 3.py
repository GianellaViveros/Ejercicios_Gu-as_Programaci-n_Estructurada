personas = 0
mujeres = 0 
varones = 0 
varones_16_a_65 = 0

mayor_datos = {
    "DNI": None,
    "Edad": -1,
    "Sexo": None }

while True:
    DNI = int(input("Ingrese DNI (Ingrese 0 si desea finalizar): "))

    if DNI == 0:
        break

    edad = int(input("Ingrese edad: "))
    sexo = input("Sexo F/M: ").upper()

    if sexo not in ['F', 'M']:
        print ("Error, ingrese 'F' o 'M'.")
        continue

    personas += 1

    if sexo == 'M':
        varones += 1
        if 16 <= edad <= 65:
            varones_16_a_65 += 1
    
    else: 
        mujeres += 1

    if edad > mayor_datos ["Edad"]:
        mayor_datos = {
        "DNI": DNI,
        "Edad": edad,
        "Sexo": sexo }

if varones > 0:
   porcentaje_varones = (varones_16_a_65 / varones) * 100
    
else: 
   porcentaje_varones = 0

print("Información obtenida del Censo")
print("Total de personas censadas: ",  (personas))
print("Total mujeres: ", (mujeres))
print("Total varones: ", (varones))
print("Porcentaje de varones entre 16 y 65 años:", round(porcentaje_varones, 2), "%")

print("Datos de la persona de mayor edad: ")
print("DNI: ", mayor_datos["DNI"])
print("Edad: ", mayor_datos["Edad"])
print("Sexo: ", mayor_datos["Sexo"])