"""
meses=0
acum=0
ingresos=0
prom=0 

while meses < 7: 
    ingresos= int(input("agregar ingresos mensuales")) 

    if ingresos < 0 :
        print(" Error el ingreso es negativo ingrese valor positivo")
        continue
    
    meses= meses+1

    acum= acum + ingresos    
    print(f"los ingresos promedio por mes es de: {acum/meses}")
"""
#otra manera mejor de hacerlo
meses=0
acum=0
ingresos=0
promedio=0

while meses < 6 : 
    ingresos= int(input("agregar ingresos mensuales"))