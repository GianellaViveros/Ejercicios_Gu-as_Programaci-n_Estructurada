producto1_precio = int(input("Ingrese el precio por Kg del producto1: "))
producto2_precio= int(input("Ingrese el precio por Kg del producto2: "))
producto3_precio= int(input("Ingrese el precio por Kg del producto3: "))

producto1_cantidad = int(input("Ingrese la cantidad por Kg del producto1: "))
producto2_cantidad = int(input("Ingrese la cantidad por Kg del producto2: "))
producto3_cantidad = int(input("Ingrese la cantidad por Kg del producto3: "))

total_producto1 = producto1_precio * producto1_cantidad
total_producto2 = producto2_precio * producto2_cantidad
total_producto3 = producto3_precio * producto3_cantidad

print ("El monto total de compra del producto1: $", round(total_producto1,2))
print ("El monto total de compra del producto2: $", round(total_producto2,2))
print ("El monto total de compra del producto3: $", round(total_producto3,2))

total = total_producto1 + total_producto2 + total_producto3
print ("El total de compras del cliente: $", round(total,2))

if total > 100: 
   descuento = total * 0.10
   nuevo_total = total - descuento
   print ("Se aplicó un descuento del 10%")
   print("El nuevo monto es: $", round(nuevo_total,2))

else: 
   print("No se aplica descuento")