Algoritmo Ejercicio_d 
	
	definir num Como Entero
	
	imprimir "ingrese un numero (entre 1 y 100): "
	leer num 
	
	//verificar si el valor es correcto
	si num < 1 O num > 100 Entonces 
		Imprimir "Error: Debe ingresar un valor entre 1 y 100"
	SiNo
		//esta dentro del rango, determinar si es par o impar 
		si num mod 2=0 entonces 
			Imprimir "El valor es par"
		SiNo
			Imprimir "El valor es impar"
		FinSi
	FinSi
	
FinAlgoritmo
