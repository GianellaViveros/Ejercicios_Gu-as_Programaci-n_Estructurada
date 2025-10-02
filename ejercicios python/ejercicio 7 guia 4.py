patentes = []
choferes = []
tipos_carga = []
horas_egreso = []

camiones_con_te = 0

for i in range(30):
    print(f"Ingreso de datos para camión {i + 1}")
    patente = input("Patente del camión: ")
    chofer = input("Nombre y apellido del chofer: ")
    
    while True:
        carga = input("Tipo de carga (madera / yerba / te): ").lower()
        if carga in ['madera', 'yerba', 'te']:
            break
        else:
            print("Error. Ingrese madera, yerba o te.")
    
    hora = input("Hora de egreso: ")
    
    patentes.append(patente)
    choferes.append(chofer)
    tipos_carga.append(carga)
    horas_egreso.append(hora)
    
    if carga == "te":
        camiones_con_te += 1

print("Informe")

for i in range(30):
    print(f"Camión {i + 1}:")
    print(f"Patente: {patentes[i]}")
    print(f"Chofer: {choferes[i]}")
    print(f"Tipo de carga: {tipos_carga[i]}")
    print(f"Hora de egreso: {horas_egreso[i]}")

print(f"Cantidad de camiones que cargaron té: {camiones_con_te}")