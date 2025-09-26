Algoritmo CalcularPromedio
	//definir variables
	Definir notapromedio, suma Como Real
	Definir condicion Como Caracter
	Definir i Como Entero
	
	Imprimir ("Ingrese valores:")
	condicion = "S" 
	Repetir
		//ingresar por teclado
//		leer nota1
//		leer nota2
//		leer nota3
//		leer nota4 
//		
//		promedio = (nota1 + nota2 + nota3 + nota4)/4
		
		Para i=1 Hasta 4 Con Paso 1 Hacer
			leer nota
			suma = suma + nota 
		Fin Para
		
		promedio = suma / 4
		
		Imprimir "El resultado es: " , promedio 
		
		Imprimir "Desea continuar? (s/n)" 
		leer condicion
		si condicion = "N" o condicion = "n" Entonces
			condicion = "N" 
		FinSi
		
	Hasta Que condicion = "N" O condicion = "n" 
	
	
FinAlgoritmo
