#Entrada
bolx=float(input("Ingrese cantidad prestada: "))
boly=float(input("Ingrese cantidad de intereses pagados: "))
t=int(input("Ingrese años que han pasado: "))
#caja negra
porc1=(boly/bolx*t)*100
#porc=(interes/bolx)*100
#Salida
print(f"El porcentaje de interes anual es: {round(porc1,2)} % ")