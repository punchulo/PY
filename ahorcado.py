import random
import mysql.connector

# Establecemos la conexión a la base de datos "ahorcado"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stitch2012",
    database="ahorcado",
)

#Cerrar sesion
def cerrar(mydb):
    if mydb:
        mydb.close()
    
# Función para crear una cuenta
def crear_cuenta(id_usuario):
    usuario = input("Ingresa un nombre de usuario: ")
    contraseña = input("Ingresa una contraseña: ")
    cursor = mydb.cursor()
    cursor.execute("INSERT INTO usuarios (id, usuario, contraseña, intentos, victorias) VALUES (%s, %s, %s, %s, %s)", (id_usuario, usuario, contraseña, 0, 0))
    mydb.commit()
    print("¡Cuenta creada con éxito!")

# Función para iniciar sesión
def iniciar_sesion():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s", (usuario, contraseña))
    resultado = cursor.fetchone()
    if resultado:
        print("¡Inicio de sesión exitoso para el usuario con ID:", resultado[0], "!")
        juego_ahorcado(resultado[0])  # Pasamos el ID del usuario al juego
    else:
        print("¡Nombre de usuario o contraseña incorrectos!")

# Función para seleccionar una palabra
def seleccionar_palabra():
    palabras = ["ordenador"]
    return random.choice(palabras)

# Función para mostrar la palabra con letras adivinadas
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

# Función para insertar una letra
def adivinar_letra():
    letra = input("Adivina una letra: ")
    return letra

# Función para el juego del ahorcado
def juego_ahorcado(usuario_id):
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 10

    while intentos > 0:
        print(mostrar_palabra(palabra, letras_adivinadas))
        letra = adivinar_letra()

        if letra in letras_adivinadas:
            print("¡Ya has usado esa letra! Intenta de nuevo.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            if set(palabra) == set(letras_adivinadas):
                print("¡Felicidades! Has adivinado la palabra: " + palabra)
                cursor = mydb.cursor()
                cursor.execute("UPDATE usuarios SET victorias = victorias + 1 WHERE id = %s", (usuario_id,))
                mydb.commit()
                cerrar(mydb)
                break
        else:
            intentos -= 1
            print("Incorrecto. Te quedan {} intentos.".format(intentos))

    if intentos == 0:
        print("¡Oh no! Te has quedado sin intentos. La palabra era: " + palabra)
        cursor = mydb.cursor()
        cursor.execute("UPDATE usuarios SET intentos = intentos + 1 WHERE id = %s", (usuario_id,))
        mydb.commit()
        cerrar(mydb)

# Código para el menú de inicio
while True:
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        id_usuario = input("Ingresa el ID del usuario: ")
        crear_cuenta(id_usuario)
    elif opcion == "2":
        iniciar_sesion()
    else:
        print("Opción no válida. Inténtalo de nuevo.")