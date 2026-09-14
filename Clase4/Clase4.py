nombre=input("nombre: ")
apellido=input("apellido: ")
email=input("email: ")

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

