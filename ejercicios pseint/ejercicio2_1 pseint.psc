Algoritmo ejercicio2_1
	
	Definir num, jubilación, obra_social, sueldo, sueldo_neto, bono Como Real
	
	jubilación = 0.11
	obra_social = 0.03
	
	Imprimir " Presione 1 si es repositor, 2 si es cajero o 3 si es supervisor "
	Leer num 
	
	Si num = 1 Entonces
		sueldo = 32335
		descuento = sueldo * (jubilación + obra_social)
		sueldo_neto = sueldo- descuento
		bono = sueldo * 0.08
		Imprimir "Sueldo Neto: $", sueldo_neto
        Imprimir "Descuento por jubilación: $", sueldo * jubilacion
        Imprimir "Descuento por obra social: $", sueldo * obra_social
        Imprimir "Bono en compras (8%): $", bono
	SiNo
		Si num = 2 Entonces
			sueldo = 38630.89
			descuento = sueldo * (jubilación + obra_social)
			sueldo_neto = sueldo - descuento
			Imprimir "Sueldo Neto: $", sueldo_neto
			Imprimir "Descuento por jubilación: $", sueldo * jubilacion
			Imprimir "Descuento por obra social: $", sueldo * obra_social
		SiNo
			Si num = 3 Entonces
			  sueldo = 45560.20
			  descuento = sueldo * (jubilación + obra_social)
			  sueldo_neto = sueldo - descuento
			  Imprimir "Sueldo Neto: $", sueldo_neto
			  Imprimir "Descuento por jubilación: $", sueldo * jubilacion
			   Imprimir "Descuento por obra social: $", sueldo * obra_social
		   SiNo
			  Imprimir "error, elija un número del 1 al 3"
		   FinSi
		FinSi
	FinSi
	
FinAlgoritmo
