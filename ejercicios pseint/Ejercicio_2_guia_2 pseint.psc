Algoritmo Ejercicio_2_guia_2
	Definir productos, canutillos, mostacillas Como Entero
	
	Imprimir "Ingrese  la cantidad de canutillos y mostacillas"
	Leer canutillos
	Leer mostacillas
	
	productos = canutillos + mostacillas
	
	Si productos < 5 Entonces
		Imprimir "No se permiten compras inferiores a 5 productos"
	Sino Si productos >= 5 y productos <= 15 Entonces
			Imprimir "El costo de envío es de $200"
		Sino si productos > 15 Entonces
				Imprimir "El envío es gratuito"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
