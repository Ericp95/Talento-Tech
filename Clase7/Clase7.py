
clientes=[]
nombre=""

while nombre != "fin":

    nombre= input("ingrese nombre del cliente")
    #clientes.append(nombre)

    if nombre == "" :
        print("nombre vacio")
        continue
    else:
        clientes.append(nombre)
        

print(clientes)