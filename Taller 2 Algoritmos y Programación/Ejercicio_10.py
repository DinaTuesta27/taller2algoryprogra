#Entradas
chelines=float(input("Ingrese la cantidad de chelines a cambiar: "))
dracmas=float(input("Ingrese la cantidad de dracmas griegos a cambiar: "))
pesetas=float(input("Ingrese la cantidad de pesetas a cambiar: "))
#Caja negra
pest=9.56871*chelines
peseta=1/0.88607
Fradg=20.110*peseta
dgfra=dracmas*1/Fradg
dolar=1*pesetas/122.499
lirasI=100*pesetas/9.289
#Salidas
print("De chelines a pesetas es:",pest)
print("De dracmas a francos es:",dgfra)
print(f"De pesetas a dolar es {dolar} y de peseta a liras italianas es {lirasI}")