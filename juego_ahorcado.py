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


def imp_pal_oculta(pala1):
    guiones =  []
    for i in range (len(pala1)):
        guiones.append("_")
    return guiones
        

# Una función para pedir al usuario que adivine una letra


def adivina_la_letra():
    letra = input("Intenta adivinar una letra: ")
    return letra


# Una función para verificar si la letra adivinada está en la palabra oculta y actualizar la palabra oculta con la letra adivinada si es el caso


def verificar_letra(palabra_original):
    letras_adivinadas =  []
    palabrita = list(imp_pal_oculta(palabra_original))
    palabra_original = list(palabra_original)
    caracter = adivina_la_letra()
    if caracter in palabra_original:
        letras_adivinadas.append(caracter)
        ind = palabra_original.index(caracter)
        palabrita[ind] = caracter
        print(f"has adivinado la letra {caracter}")
    else: 
        print(f"La letra {caracter} no está en la palabra")
    for  i in  palabrita:
        print(i,end='')


# Una función para dibujar una parte del cuerpo del ahorcado cada vez que el usuario adivina una letra incorrecta


#La función principal/main


def run():
    x = palabra_aleatoria()
    y = imp_pal_oculta(x)
    while "_" in list(y) :
        verificar_letra(x)


# Nos aseguramos de que el código se ejecute solo cuando se ejecuta el archivo Python directamente, y no cuando se importa desde otro archivo Python.


if __name__ == "__main__":
    run()