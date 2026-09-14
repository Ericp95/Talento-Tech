nombre=input("nombre: ")
apellido=input("apellido: ")
edad=int( input("edad: "))
email=input("email: ")

if nombre == "" :
    print("ERROR")
else:
    print(nombre)


if apellido == "" :
    print("ERROR")
else:
    print(apellido)


if edad < 18 :
    print("ERROR")
else:
    print(edad)


if email == "" :
    print("ERROR")
else:
    print(email)
