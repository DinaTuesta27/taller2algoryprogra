#Entradas
horastrabajadas=int(input("Ingrese cantidad de horas trabajadas: "))
valorhora=float(input("Ingrese valor de hora trabajada: ")) 
#Caja Negra
sueldo=valorhora*horastrabajadas
desc=sueldo*0.20
total=sueldo-desc
#Salidas
print("El sueldo a pagar es:",total)