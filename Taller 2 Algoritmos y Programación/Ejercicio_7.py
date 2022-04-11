#Entrada
metros=float(input("Ingrese cantidad de metros a transformar: "))
#Caja Negra
pulgadas=metros*39.27
pies=pulgadas/12
#Salidas
print(f"{metros} metros es igual a {round(pulgadas,2)} pulgadas y a {round(pies,2)} pies.")