
lista= input("ingrese nombres que desea listar")
array=lista.split()

for i in range(len(array)): 
    print(f" Cliente{i+1}: {array[i]}")