Algoritmo ejercicio3
	Definir  matriz_notas Como Entero
	Definir promedio Como Real
	
	Dimension matriz_notas[40,5]
	Dimension promedio[40] //vector donde se guardan los promedios
	
	Definir fil, col Como Entero
	
	//recorrer la matriz_notas
	para fil = 0 Hasta 39 Hacer//filas o alumnos
		para col = 0 Hasta 4 Hacer //columnas o notas
			matriz_notas[fil,col] = aleatorio(1,10) 
			Imprimir Sin Saltar matriz_notas[fil,col], " "
		FinPara
		Imprimir " " 
	FinPara
FinAlgoritmo
