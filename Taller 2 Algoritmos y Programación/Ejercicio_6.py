#Entrada
mujeres=int(input("Ingrese cantidad de mujeres: "))
hombres=int(input("Ingrese cantidad de hombres: "))
#Caja negra
total_de_estudiantes=mujeres+hombres #int
mp=mujeres*100/total_de_estudiantes #float
hp=hombres*100/total_de_estudiantes #float
#Salidas
print(f"El porcentaje de mujeres: {round(mp,2)} y el porcentaje de hombres es: {round(hp,2)}") 
#round es para redondear y el num es para cantidad de decimales