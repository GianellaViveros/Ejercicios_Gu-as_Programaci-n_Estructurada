Algoritmo Mayor_menor 
	Definir numero, mayor, menor Como Entero
    Definir primer_valor Como Logico
    primer_valor <- Verdadero
	
    Escribir "Ingrese una secuencia de números"
	
    Repetir
        Leer numero
		
        Si numero <> -1 Entonces
            Si numero < 0 Entonces
                Escribir "Error: ingresó un valor no permitido, intente de nuevo."
            Sino
                Si primer_valor Entonces
                    mayor <- numero
                    menor <- numero
                    primer_valor <- Falso
                Sino
                    Si numero > mayor Entonces
                        mayor <- numero
                    FinSi
                    Si numero < menor Entonces
                        menor <- numero
                    FinSi
                FinSi
            FinSi
        FinSi
    Hasta Que numero = -1
	
    Si primer_valor = Falso Entonces
        Escribir "El mayor valor es: ", mayor
        Escribir "El menor valor es: ", menor
    Sino
        Escribir "No se ingresaron valores válidos."
    FinSi
FinProceso