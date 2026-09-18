
#lista= input("ingrese nombres que desea listar")
#array=lista.split()
"""nombres=["pedro", "juan","pablo","eric","", "juanita","lola"]

for i in range(len(nombres)): 
    if nombres[i] == "":
        print(f" Cliente{i+1}: Error nombre vacio")
    else:
        print(f" Cliente{i+1}: {nombres[i].capitalize()}")
"""
#haciendo una forma mejor


n=int(input("ingrese cantidad de clientes que quiere listar"))
clientes=[]


for i in range(len(n)) :
    nombres= input("ingrese nombres de los clientes a listar")
    clientes.append(nombres)


