#Entrada
galon=int(input("Ingrese los galones suministrados: "))
#Caja negra
litros=galon*3.785
pesos=litros*50000
#Salida
print(f"El total a pagar por galon es: {pesos} COP")