"""
Procesamiento del grupo de imagenes selfies, deben estar alojado en
una carpeta o en una dirección de almacenamiento
"""
import os
import random
from PIL import Image
from colorama import init, Back, Fore, Style

# abrir archivo de selfies
def abrir_fileImagen(carpetaftp, re_ancho, re_alto, cantidad_subdivisiones):
    # contar cuantos archivos existen en la carpeta
    contador = 0
    for archivo in os.listdir(carpetaftp):
        if archivo.endswith(('.png', '.jpg', '.jpeg')):
            contador += 1

    # Listar archivos de imágenes en la carpeta
    imagenes = [f for f in os.listdir(carpetaftp) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # si en la carpeta ftp de selfies hay igual o mayor cantidad de archivos que se va a necesitar
    if contador >= cantidad_subdivisiones:
        # Seleccionar la cantidad de imágenes aleatorias disponibles
        imagenes_seleccionadas = random.sample(imagenes, cantidad_subdivisiones)
        
        new_imagenes = [] # Crear una lista vacia para almacenar las imágenes convertidas

        # Cargar y redimensionar las imágenes seleccionadas
        for nombre_imagen in imagenes_seleccionadas:
            ruta_imagen = os.path.join(carpetaftp, nombre_imagen)
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((int(re_ancho), int(re_alto)))  # Redimensionar según el tamaño deseado
            new_imagenes.append(imagen)
        
        return new_imagenes
    else:
        init()
        print(Fore.RED+Back.WHITE+' CANTIDAD INSUFICIENTE DE SELFIES '+Style.RESET_ALL)

