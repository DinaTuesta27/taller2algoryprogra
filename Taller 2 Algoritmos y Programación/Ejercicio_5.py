#Entrada
Parcial1=float(input("Ingrese nota de parcial 1: "))
Parcial2=float(input("Ingrese nota de parcial 2: "))
Parcial3=float(input("Ingrese nota de parcial 3: "))
Examenfinal=float(input("Ingrese nota del parcial final: "))
Trabajofinal=float(input("Ingrese calificación de trabajo final: "))
#Caja Negra
promparsf=(Parcial1+Parcial2+Parcial3)/3
porprompar=promparsf*0.55
porexamf=Examenfinal*0.30
portrab=Trabajofinal*0.15
totalcalif=porprompar+porexamf+portrab
#Salida
print(f"Nota final de la materia: {round(totalcalif,2)}")