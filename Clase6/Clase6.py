
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


n=input("ingrese cantidad de clientes que quiere listar")
clientes=[]


for i in range(len(n)) :
    nombres= input(f"ingrese nombres de los cliente:")
    clientes.append(nombres)

    if clientes[i] == "" :
        print(f"cliente {i+1}: ERROR nombre vacio")
    
print(f" Cliente{i+1}: {clientes[i].capitalize()}")


