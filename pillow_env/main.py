# -*- coding: utf-8 -*-
from PIL import Image, ImageChops, ImageEnhance, ImageOps

def main():

    #Esto abre una imagen que esté dentro de nuestro proyecto
    imagen = Image.open('imagen.jpg')
    imagen_2 = Image.open('imagen_2.jpg')
    #Esta linea hace que muestre la foto cuando se ejecute el programa
    imagen.show()

    #Ejemplo para invertir los colores de la imagen
    new_imagen = ImageChops.invert(imagen)
    new_imagen.save("imagen_2.jpg")

    #Ejemplo para cambiar la escala de grises de la imagen
    new_imagen = ImageOps.grayscale(imagen)
    new_imagen.save("imagen_3.jpg")

    #Ejemplo para subir el brillo de la imagen
    new_imagen = ImageEnhance.Brightness(imagen).enhance(2)
    new_imagen.save("imagen_4.jpg")

    #Ejemplo para aumentar el contraste de la imagen
    new_imagen = ImageEnhance.Contrast(imagen).enhance(4)
    new_imagen.save("imagen_5.jpg")

    #Ejemplo para voltear una imagen como si fuera un espejo
    new_imagen = ImageOps.mirror(imagen)
    new_imagen.save("imagen_6.jpg")

    #Cambia el tamaño de la imagen
    new_imagen = imagen.resize((320, 240))
    new_imagen.save("imagen_7.jpg")

    #Ejemplo para disminuir la tinidez de la imagen
    new_imagen = ImageEnhance.Sharpness(imagen).enhance(-4)
    new_imagen.save("imagen_8.jpg")

    # Devuelve el valor absoluto de la diferencia píxel por píxel entre las dos imágenes.
    new_imagen = ImageChops.difference(imagen, imagen_2)
    new_imagen.save('imagen_9.jpg')


if __name__ == "__main__":
    main()
