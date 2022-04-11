#Entradas
sueldo=int(input("Ingrese sueldo: "))
venta1=int(input("Ingrese primera venta: "))
venta2=int(input("Ingrese segunda venta: "))
venta3=int(input("Ingrese tercera venta: "))
#Caja negra
comit=(venta1+venta2+venta3)*0.10
stm=comit+sueldo
#Salida
print(f"El sueldo total con comisiones es: {stm}")