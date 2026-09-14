nombre=input("nombre: ")
apellido=input("apellido: ")
email=input("email: ")
edad=int( input("edad: "))

if nombre == "" :
    print("ERROR")
else:
    print(nombre.capitalize())

if apellido == "" :
    print("ERROR")
else:
    print(apellido.capitalize())

if email.count('@') == 1:
    print(email.strip())
else:
    print("ERROR")


if edad > 18:
    print("es un adulto")
elif edad <= 15 :
    print ("es un niño/a")
elif edad > 15 and edad <=18:
    print("es un adolescente")
else:
    print("ERROR")
