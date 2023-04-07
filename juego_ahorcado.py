# Programa para jugar al ahorcado. El objetivo del juego es adivinar una palabra oculta 
# antes de que se dibuje una figura completa del ahorcado.


import random


# Una función para seleccionar una palabra aleatoria de una lista predefinida


def palabra_aleatoria():
    palabras = ["Computadora","Libro","Jardín","Montaña","Océano","País","Perro","Gato","Tren","Avión","Lápiz","Bolígrafo","Reloj","Cama","Silla","Mesa",
   "Cielo","Estrella","Luna","Sol","Pescado","Guitarra","Piano","Violín","Fútbol","Baloncesto","Tenis","Natación","Yoga","Cine","Teatro","Arte",
   "Ciencia","Historia","Matemáticas","Geografía","Literatura","Música","Política","Economía","Cocina","Moda","Belleza","Viajes","Naturaleza",
   "Fotografía","Tecnología","Teléfono","Internet","Redes sociales"]
    selected = random.choice(palabras)
    return selected


# Una función para mostrar la palabra oculta, con cada letra representada por un guión bajo


def imp_pal_oculta(pala1):
    for i in range (len(pala1)):
        print("-",end='') 


# Una función para pedir al usuario que adivine una letra


def adivina_la_letra(palabrita,palabra_original):
    palabrita = list(palabrita)
    palabra_original = list(palabra_original)
    while True:
        caracter = input("Escribe una letra: ")
        if caracter in palabra_original:
            ind = palabra_original.index(caracter)
            
            print("has adivinado la letra {caracter}") in on my de
            break


# Una función para verificar si la letra adivinada está en la palabra oculta y actualizar la palabra oculta con la letra adivinada si es el caso


# Una función para dibujar una parte del cuerpo del ahorcado cada vez que el usuario adivina una letra incorrecta


#La función principal/main


def run():
    x = palabra_aleatoria()
    print(x)
    imp_pal_oculta(x)
    print("Ten un buen día!")


if __name__ == "__main__":
    run()
    