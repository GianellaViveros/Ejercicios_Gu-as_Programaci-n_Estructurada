vendedores = []
ventas = []

for i in range(15):
    nombre = input(f"Ingrese el nombre del vendedor {i + 1}: ") 
    venta = float(input(f"Ingrese la venta en dólares de {nombre}: "))
    vendedores.append(nombre)
    ventas.append(venta)

indice_mayor = ventas.index(max(ventas))
indice_menor = ventas.index(min(ventas))

dolar_a_pesos = 140
mayor_venta_dolares = ventas[indice_mayor]
mayor_venta_pesos = mayor_venta_dolares * dolar_a_pesos

menor_venta_dolares = ventas[indice_menor]
menor_venta_pesos = menor_venta_dolares * dolar_a_pesos

print("Informe")
print(f"El vendedor con la mayor venta: {vendedores[indice_mayor]}")
print(f"Venta: $ {mayor_venta_dolares} USD / $ {mayor_venta_pesos} pesos")
print(f"El vendedor con la menor venta: {vendedores[indice_menor]}")
print(f"Venta: $ {menor_venta_dolares} USD / $ {menor_venta_pesos} pesos")
