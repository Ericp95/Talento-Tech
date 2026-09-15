meses=0
acum=0
ingresos=0
prom=0 

while meses < 6: 
    ingresos= int(input("agregar ingresos mensuales")) 

    if ingresos < 0 :
        print(" Error el ingreso es negativo ingrese valor positivo")
        continue

    if ingresos > 0 :
        acum= acum + ingresos
        meses= meses+1

    print(f"los ingresos promedio por mes es de: {acum/meses}")
