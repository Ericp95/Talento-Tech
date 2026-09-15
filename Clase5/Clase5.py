meses=0
acum=0
ingresos=0
prom=0 

while meses < 6: 
    ingresos= int(input("agregar ingresos mensuales")) 

    if ingresos < 0 :
        print(" Error el ingreso es negativo")

    if ingresos > 0 :
        acum= acum + ingresos
        meses= meses+1
        
