#Entradas
x=float(input("Ingrese valor invertido en lote de naranjas: "))
y=float(input("Ingrese valor por docena de naranjas: "))
k=float(input("Ingrese las ganancias generadas: "))
#Caja Negra
goi=(k/(x+y))*100
#Salida
print("El porcentaje de ganancia obtenida es de:",goi)