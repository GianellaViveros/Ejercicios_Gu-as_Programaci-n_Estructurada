DNI = int(input("Ingrese su DNI:")) 
categoría = int(input("Ingrese la categoría a la que pertenece:")) 

sueldo_0 = 23600 
sueldo_1 = 35800 
sueldo_2 = 60420 

descuento_jubilacion = 0.11 
descuento_obra_social0 = 0.03 
descuento_obra_social1 = 0.05 
descuento_obra_social2= 0.05
descuento_club_2 = 0.04 

total_descuento_0 = descuento_jubilacion + descuento_obra_social0 
total_descuento_1 = descuento_jubilacion + descuento_obra_social1 
total_descuento_2 = descuento_jubilacion + descuento_obra_social2 + descuento_club_2 

sueldo_neto_0 = sueldo_0 - (sueldo_0 * total_descuento_0)
sueldo_neto_1 = sueldo_1 - (sueldo_1 * total_descuento_1)
sueldo_neto_2 = sueldo_2 - (sueldo_2 * total_descuento_2) 

if categoría == 0:
    categoria_nombre = "Maestranza"
    sueldo_neto = sueldo_neto_0

elif categoría == 1:
    categoria_nombre = "Administración"
    sueldo_neto = sueldo_neto_1

elif categoría == 2:
    categoria_nombre = "Gerencia"
    sueldo_neto = sueldo_neto_2

else:
    categoria_nombre = None

if categoria_nombre:
    print("Su DNI es:", DNI)
    print("Su categoría es:", categoria_nombre)
    print("Su sueldo neto es: $", round(sueldo_neto, 2))
else:
    print("Error, ponga el número según corresponda su categoría")