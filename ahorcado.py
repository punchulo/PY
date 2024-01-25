import random
import mysql.connector

#Establecemos la conexion a la base de datos "ahorcado".
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="stitch2012",
  database="ahorcado",

)

#Selecciona una de las palabras en la lista.
def seleccionar_palabra():
    palabras = ["ordenador"]
    return random.choice(palabras)

#Muestra la palabra cambiando los caracteres por "_ ".
def mostrar_palabra(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

#Insertaremos las letras.
def adivinar_letra():
    letra = input("Adivina una letra: ")
    return letra

#Empieza el juego
def juego_ahorcado():
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos = 10
    
 #mientras aun queden intentos te dejara seguir.
    while intentos > 0:
        print(mostrar_palabra(palabra, letras_adivinadas))
        letra = adivinar_letra()

#Si la letra es adivinada cambia el caracter correspondiente por la letra, si la letra ya esta en uso te avisa y te deja seguir intentandolo y al adivinar todas las letras te felicita.
        if letra in letras_adivinadas:
            print("Ya has usado esa letra. Intenta de nuevo.")
        elif letra in palabra:
            letras_adivinadas.append(letra)
            if set(palabra) == set(letras_adivinadas):
                print("¡Felicidades! La palabra era: " + palabra)
                break
              
#Si nos equivocamos nos resta un intento.
        else:
            intentos -= 1
            print("Incorrecto. Quedan {} intentos.".format(intentos))
            
#Si nos quedamos sin intentos nos enseña cual era la palabra.
    if intentos == 0:
        print("Fin del juego. La palabra era: " + palabra)

juego_ahorcado()