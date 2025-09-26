canutillos = int(input("Ingrese la cantidad de canutillos:"))
mostacillas = int(input("Ingrese la cantidad de mostacillas:"))
productos = (canutillos + mostacillas)

if productos < 5:
    print("No se permiten com0pras inferiores a 5")

elif productos  >= 5 and productos <= 15:
    print("El costo de envío es $200")

else:
    print ("EL envío es gratis")
