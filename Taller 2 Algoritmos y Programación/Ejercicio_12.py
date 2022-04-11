#entradas
#Matematicas
ExamenM=float(input("ingrese la nota del examen de matematicas: "))
Tarea1_M=float(input("Ingrese la nota de la tarea 1 de matematicas: "))
Tarea2_M=float(input("Ingrese la nota de la tarea 2 de matematicas: "))
Tarea3_M=float(input("Ingrese la nota de la tarea 3 de matematicas: "))
#Fisica
ExamenF=float(input("ingrese la nota del examen de Fisica: "))
Tarea1_F=float(input("Ingrese la nota de la tarea 1 de Fisica: "))
Tarea2_F=float(input("Ingrese la nota de la tarea 2 de Fisica: "))
#Quimica
ExamenQ=float(input("ingrese la nota del examen de Quimica: "))
Tarea1_Q=float(input("Ingrese la nota de la tarea 1 de Quimica: "))
Tarea2_Q=float(input("Ingrese la nota de la tarea 2 de Quimica: "))
Tarea3_Q=float(input("Ingrese la nota de la tarea 3 de Quimica: "))
#Caja negra
Promedio_M=ExamenM*0.90+((Tarea1_M+Tarea2_M+Tarea3_M)/3)*0.10
Promedio_F=ExamenF*0.80+((Tarea1_F+Tarea2_F)/2)*0.20
Promedio_Q=ExamenQ*0.85+((Tarea1_Q+Tarea2_Q+Tarea3_Q)/3)*0.15
Promedio_general=round((Promedio_M+Promedio_F+Promedio_Q)/3 ,2)
#Salidas
print("Su promedio general es de: ", Promedio_general)