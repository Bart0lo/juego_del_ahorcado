# Programa para jugar al ahorcado. El objetivo del juego es adivinar una palabra oculta 
# antes de que se dibuje una figura completa del ahorcado.

#Importamos la libreria random para usarla en nuestra primera función


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


def mostrar_palabra_oculta(palabra, letras_adivinadas):
    resultado = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + ' '
        else:
            resultado += '_ '
    return resultado


# Una función para pedir al usuario que adivine una letra


def adivina_la_letra():
    letra = input("Intenta adivinar una letra: ")
    return letra


# Una función para verificar si la letra adivinada está en la palabra oculta y actualizar la palabra oculta con la letra adivinada si es el caso

def comprobar_letra(letra, palabra, letras_adivinadas):
    if letra in palabra:
        letras_adivinadas.append(letra)
        return True
    else:
        return False


# Una función para dibujar una parte del cuerpo del ahorcado cada vez que el usuario adivina una letra incorrecta

#YA lo hice
#La función principal/main


def run():
    x = palabra_aleatoria()
    y = imp_pal_oculta(x)
    z  = verificar_letra(y, x)


# Nos aseguramos de que el código se ejecute solo cuando se ejecuta el archivo Python directamente, y no cuando se importa desde otro archivo Python.


if __name__ == "__main__":
    run()