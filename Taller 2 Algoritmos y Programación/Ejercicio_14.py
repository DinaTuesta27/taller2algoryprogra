#Entrada
lectante=float(input("Ingrese la lectura anterior (kv): "))
lectactu=float(input("Ingrese la lectura actual (kv): "))
costok=float(input("Ingrese el costo por kilovatio: "))
#Caja Nerga
promlec=(lectante+lectactu)/2
total=promlec*costok
#Salida
print("El monto a pagar este mes es de:",total)