"""
Procesamiento de la imagen que ira detras de las imagenes de selfies
"""
from PIL import Image
import os
# abrir la imagen principal, obtener dimensiones de la imagen
def abrir_imagen(imagen_dir):
    # obtener la extension del archivo
    extension = os.path.splitext(imagen_dir)[1].lower()

    # verificar la extension del archivo de imagen
    if extension == '.png':
        # abrir la imagen png
        imagen = Image.open(imagen_dir)
        # Convertir a modo RGB para asegurarse de que sea compatible con JPG
        imagen = imagen.convert('RGB')
        dim_x = imagen.width
        dim_y = imagen.height
        return imagen, dim_x,dim_y
    else:
        abrir_imagen = Image.open(imagen_dir)
        dim_x = abrir_imagen.width
        dim_y = abrir_imagen.height
        return abrir_imagen, dim_x,dim_y

# funcion para obtener coordenads
def posicion_imagen(dim_x, dim_y, div_x, div_y):
    array_x = [0] # se guarda coordenadas en x
    array_y = [0] # se guarda coordenadas en y
    addx = 0
    addy = 0
    cantidad_selfis = div_x * div_y # cantidad de fotografias disponibles
    pos_x = dim_x/div_x # division de la imagen
    pos_y = dim_y/div_y

    # creacion de las coordenadas
    for i in range(div_x-1):
        addx = int(addx + pos_x)
        array_x.append(addx)
    
    for i in range(div_y-1):
        addy = int(addy + pos_y)
        array_y.append(addy)

    return cantidad_selfis, array_x, array_y, pos_x, pos_y
