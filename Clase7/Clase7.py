
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
        

#print(clientes)

for i in clientes:
    clientes.sort()
    
    print(f"Lista de Clientes: {clientes}")

    break
