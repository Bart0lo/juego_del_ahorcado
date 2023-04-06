# Una idea de proyecto en Python que no incluya librerías podría ser un 
# programa para jugar al ahorcado. El objetivo del juego es adivinar una palabra oculta 
# antes de que se dibuje una figura completa del ahorcado. El programa podría tener las siguientes funciones:

# Una función para seleccionar una palabra aleatoria de una lista predefinida
# Una función para mostrar la palabra oculta, con cada letra representada por un guión bajo
# Una función para pedir al usuario que adivine una letra
# Una función para verificar si la letra adivinada está en la palabra oculta y actualizar la palabra oculta con la letra adivinada si es el caso
# Una función para dibujar una parte del cuerpo del ahorcado cada vez que el usuario adivina una letra incorrecta
# Para implementar este programa, podrías utilizar algunas estructuras básicas de Python, como las listas, las cadenas de texto, los 
# condicionales y los bucles. 
# También podrías utilizar la función input() para obtener la entrada del usuario y la función print() 
# para mostrar el estado del juego en la pantalla.
import random


def palabra_aleatoria():
    palabras = ["Computadora","Libro","Jardín","Montaña","Océano","País","Perro","Gato","Tren","Avión","Lápiz","Bolígrafo","Reloj","Cama","Silla","Mesa",
   "Cielo","Estrella","Luna","Sol","Pescado","Guitarra","Piano","Violín","Fútbol","Baloncesto","Tenis","Natación","Yoga","Cine","Teatro","Arte",
   "Ciencia","Historia","Matemáticas","Geografía","Literatura","Música","Política","Economía","Cocina","Moda","Belleza","Viajes","Naturaleza",
   "Fotografía","Tecnología","Teléfono","Internet","Redes sociales"]
    selected = random.choice(palabras)
    return selected


def imp_pal_oculta(pala1):
    for i in range (len(pala1)):
        print("-",end='') 


def adivina_la_letra(palabrita):
    palabrita = list(palabrita)
    while True:
        caracter = input("Escribe una letra: ")
        if caracter in pal2:
            print("has adivinado la letra {caracter}")
            break


def run():
    x = palabra_aleatoria()
    print(x)
    imp_pal_oculta(x)


if __name__ == "__main__":
    run()
    