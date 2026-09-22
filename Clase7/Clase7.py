
clientes=[]

while nombre == "fin":

    nombre= input("ingrese nombre del cliente")
    clientes.append(nombre)

    if nombre == "" :
        print("nombre vacio")