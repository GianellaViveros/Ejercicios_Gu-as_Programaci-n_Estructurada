CANT = []         
Total = [0] * 15  

print("Carga de la matriz CANT (50 artículos x 15 vendedores)")
for i in range(50):  
    fila = []
    print(f"Artículo {i + 1}:")
    for j in range(15):  
        cantidad = int(input(f"Cantidad vendida por el vendedor {j + 1}: "))
        fila.append(cantidad)
    CANT.append(fila)

for j in range(15): 
    total_vendedor = 0
    for i in range(50):  
        total_vendedor += CANT[i][j]
    Total[j] = total_vendedor

mayor_venta = max(Total)
vendedor_max = Total.index(mayor_venta) + 1 

print("Total por vendedor")
for j in range(15):
    print(f"Vendedor {j + 1}: {Total[j]} artículos vendidos")

print(f"El vendedor que realizó la mayor venta fue el vendedor {vendedor_max} con {mayor_venta} artículos vendidos.")