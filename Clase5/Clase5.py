meses=1
acum=0
ingresos=0
prom=0 

while meses < 7 : 
    ingresos= int(input("agregar ingresos mensuales")) 

    if ingresos < 0 :
        print(" Error el ingreso es negativo")
        
