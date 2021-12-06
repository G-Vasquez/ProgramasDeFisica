print ("Programa en Python...")
print ("Prgrama que calcula el promedio de un estudiante")
print ("Ingrese la calificacion de las siguientes materias:")

Metrologia = float(input("Metrologia:"))
Algebra = float (input("Algebra:"))
Calculo = float (input("Calculo:"))
Economia = float (input("Economia:"))
Estadistica = float (input("Estadistica:"))
EstudioTrabajo = float (input("Estudio de Trabajo:"))

PromedioFinal = (Metrologia+Algebra+Calculo+Economia+Estadistica+EstudioTrabajo)/6

print ("El promedio final de Alumno es:" + str(PromedioFinal))
