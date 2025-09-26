Algoritmo promedio_alumnos
	// estructura Mientras
	
	Definir edad Como Entero
	Definir acum_edades Como Entero
	Definir contador_alumno Como Entero
	Definir promedio_edades Como Real
	Definir  flag Como Logico
	Definir cant_alumnos Como Entero
	
	
	Escribir "Ingrese la edad del alumno (pulse 0 para terminar)" 
	
	//Para 
	Escribir "Ingrese cantidad de alumnos:"
	Leer cant_alumnos
	
	Para i = 1 hasta cant_alumnos Con Paso 1 Hacer
		
	FinPara
	
	flag = Verdadero
	Repetir 
		leer edad
		escribir "la edad es:", edad
		
		si edad = 0 Entonces
			flag = falso 
		SiNo
			contador_alumno = contador_alumno + 1 //voy contando la cantidad de alumnos
			acum_edades = acum_edades + edad // voy acumulando o sumando las edades 
		FinSi
	hasta que flag = Falso
	
	promedio_edades = acum_edades / contador_alumno
	
	Escribir "cantidad de alumno:" , contador_alumno
	Escribir "suma de edades:", acum_edades
	
	Escribir "El promedio de edades es:", promedio_edades
	
FinAlgoritmo
