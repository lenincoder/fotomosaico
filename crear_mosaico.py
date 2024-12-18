"""
Sobrepone la imagen principal con las imagenes selfies
"""
from colorama import init, Back, Fore, Style
from PIL import Image, ImageEnhance

def unir_imagenes(imagenes, ancho, alto, matriz_x, matriz_y):
    if len(imagenes) < len(matriz_x) * len(matriz_y):
        init()
        print(Fore.RED+Back.WHITE+' CANTIDAD INSUFICIENTE DE SELFIES '+Style.RESET_ALL)
    else:
        i = 0
        nueva_imagen = Image.new('RGBA', (ancho, alto), (255, 255, 255, 0)) # Fondo transparente

        # colocar imagenes en cuadriculas
        for fila in matriz_y:
            for columna in matriz_x:
                nueva_imagen.paste(imagenes[i], (columna, fila))
                i += 1
        return nueva_imagen

# funcion para agregar transparencia a la imagen
def agregar_transparencia(imagen, transparencia):
    if 0 <= transparencia <= 255:
        alpha = imagen.getchannel('A')
        alpha = alpha.point(lambda p:p * (transparencia / 255))
        imagen.putalpha(alpha)
    else:
        init()
        print(Fore.RED+Back.WHITE+' LA TRANSPARENCIA DEBE ESTAR ENTRE 0 y 255 '+Style.RESET_ALL)
    return imagen

# funcion para ajustar el constraste de una imagen
def ajustar_contraste(imagen, factor_contrarte):
    # crear un oobjeto ImageEnhance para el contraste
    enhancer = ImageEnhance.Contrast(imagen)
    # Ajustar el contraste de la imagen con el factor dado
    imagen_mejorada = enhancer.enhance(factor_contrarte)
    return imagen_mejorada

def fusion(imagen1, imagen2):
    imagen1.paste(imagen2, (0, 0), mask = imagen2)
    return imagen1