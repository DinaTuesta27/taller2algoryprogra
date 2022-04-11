#Entrada
pvp=float(input("Ingrese precio de venta al publico: "))
pf=float(input("Ingrese precio final pagado: "))
#Caja negra
desc=((pf-pvp)/pvp)*(-1)
descf=desc*100
#Salida
print(f"El porcentaje de descuento aplicado es de: {descf}%")