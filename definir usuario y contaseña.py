# Definir el usuario y la contraseña correctos
usuariot = "pablo"
contraseñat = "1234"

# Pedir al usuario que ingrese su usuario y contraseña
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

# Verificar si el usuario y la contraseña son correctos
if usuariot == usuario and contraseñat == contraseña:
    print("Ha entrado en el sistema.")
else:
    print("No ha entrado en el sistema")