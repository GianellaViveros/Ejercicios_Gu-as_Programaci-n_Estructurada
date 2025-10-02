def esta_aprobado(nota1, nota2, nota3):
    if nota1 > 4 and nota2 > 4 and nota3 > 4:
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 7:
            return "El alumno está aprobado."
        else:
            return "El alumno no está aprobado (promedio menor a 7)."
    else:
        return "El alumno no está aprobado (alguna nota menor o igual a 4)."

print("Ingrese las tres notas del alumno:")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

resultado_usuario = esta_aprobado(nota1, nota2, nota3)
print(f"Resultado para las notas ingresadas: {resultado_usuario}")

print("Prueba de escenarios")
escenarios = [
    (3, 9, 9),
    (6, 8, 10)]

for i, (n1, n2, n3) in enumerate(escenarios, start=1):
    resultado = esta_aprobado(n1, n2, n3)
    print(f"Escenario {i}: Notas = {n1}, {n2}, {n3} → {resultado}")