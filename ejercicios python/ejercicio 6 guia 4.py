n = int(input("Ingrese la cantidad de productos: "))

cantidades = []
costos = []

for i in range(n):
    cantidad = int(input(f"Ingrese la cantidad del producto {i + 1}: "))
    costo = float(input(f"Ingrese el costo del producto {i + 1}: "))
    cantidades.append(cantidad)
    costos.append(costo)

precios_totales = []
precio_total_general = 0

print("Productos que superan los $1000")
for i in range(n):
    precio_producto = cantidades[i] * costos[i]
    precios_totales.append(precio_producto)
    precio_total_general += precio_producto

    if precio_producto > 1000:
        print(f"Producto {i + 1} -> Cantidad: {cantidades[i]}, Costo: ${costos[i]} -> Total: ${precio_producto:.2f}")

# Paso 5: Mostrar precio total general
print(f"Precio total general de los productos: ${precio_total_general:.2f}")