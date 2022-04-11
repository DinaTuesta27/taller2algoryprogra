#Entradas
from pydoc import pager
from xml.dom import NoModificationAllowedErr


nombre=str(input("Ingrese su nombre: "))
horastrab=int(input("Ingrese cantidad de horas trabajadas: "))
pagonorm=float(input("Ingrese valor del pago por hora: "))
horasext=int(input("Ingrese cantidad de horas extra trabajadas: "))
hijos=int(input("Ingrese cantidad de hijos: "))

#Caja Negra
sueldob=horastrab*pagonorm
paghext=pagonorm+((horasext*pagonorm)*0.25)
actualaca=250000
prima=180000
sueldot=actualaca+prima+(173000*hijos)+paghext
deduc=sueldob-(sueldob*0.14)
sueldoneto=deduc+sueldot
#Salidas
print(nombre)
print("El sueldo neto es de:",sueldoneto)
print("El pago por horas extra es:",paghext)
print("Las deducciones son de:",deduc)