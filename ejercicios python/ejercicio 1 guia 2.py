#definición de variables
jubilacion = 0.11
obra_social = 0.03
# Solicitar al usuario el tipo de empleado
num = int(input("Presione 1 si es repositor, 2 si es cajero o 3 si es supervisor:"))

if num == 1:
    sueldo = 32335
    descuento = sueldo * (jubilacion + obra_social)
    sueldo_neto = sueldo - descuento
    bono = sueldo * 0.08
    print ("Sueldo Neto: $", round(sueldo_neto,2))
    print ("Descuento por jubilación: $", round(sueldo * jubilacion,2))
    print ("Descuento por obra social: $", round(sueldo * obra_social,2))
    print ("Bono en compras (8%): $", round(bono,2))

elif num == 2: 
    sueldo = 38630.89 
    descuento = sueldo * (jubilacion + obra_social)
    sueldo_neto = sueldo - descuento 
    print ("Sueldo Neto: $", round(sueldo_neto,2))
    print ("Descuento por jubilacion: $", round(sueldo * jubilacion,2))
    print ("Descuento por obra social: $", round(sueldo * obra_social,2))

elif num == 3:
    sueldo = 45560.20 
    descuento = sueldo * (jubilacion + obra_social)
    sueldo_neto = sueldo - descuento
    print ("Sueldo Neto: $", round(sueldo_neto,2))
    print ("Descuento por jubilacion: $", round(sueldo * jubilacion,2))
    print ("Descuento por obra social: $", round(sueldo * obra_social))
    
else:
    print ("Error, elija un número del 1 al 3")