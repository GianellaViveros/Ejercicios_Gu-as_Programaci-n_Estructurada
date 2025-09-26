for cliente in range (1,6):
    print(cliente)

    DNI = (input("Ingrese su DNI:"))
    servicio = int(input("Ingrese el tipo de servicio (1 = 30 megas, 2 = 50 megas, 3 = 100 megas):"))

    if servicio == 1:
      nombre_servicio = "Internet 30 megas"
      costo = 750
      print("El costo es: $", costo)
   
    elif servicio == 2:
      nombre_servicio = "Internet 50 megas"
      costo = 1100
      print("El costo es: $", costo)
   

    elif servicio == 3:
       nombre_servicio = "Internet 100 megas"
       costo = 1500
       costo -= costo * 0.05
       print("El costo es: $", round(costo,2))

    else:
        print("Tipo de servicio no válido")
        continue
   
    print("Su DNI es:", DNI)
    print("El servicio con el que cuenta es:", nombre_servicio)
   