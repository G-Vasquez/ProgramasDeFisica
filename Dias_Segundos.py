print ("Programa en Python....")
print ("Programa que convierta dias a segundos")

Minuto = 60
Hora = 60*Minuto
Dia = Hora*24

NumDias = int (input("Ingresa el numero de dias a convertir:"))

TotalSegundos = Dia*NumDias

print ("El total de segundos es:"+ str(TotalSegundos) + " " + "Segundos")
