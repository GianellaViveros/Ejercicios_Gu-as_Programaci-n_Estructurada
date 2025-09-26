Algoritmo Vectores

	// Definir variables
	
	Definir vector Como Entero
	Definir i, suma Como Entero
	
	suma = 0
	
	Escribir "El vector aleatorio es:"
	
	Para i = 0 Hasta 9 Con Paso 1 Hacer
		vector = Aleatorio(1, 20)
		Escribir Sin Saltar vector, " "
		suma = suma + vector
	FinPara
	
	Escribir "La suma total es: ", suma
	
FinAlgoritmo
