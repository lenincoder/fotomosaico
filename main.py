import pri_imagen
import selfie_imagen
import crear_mosaico
from colorama import Back, Fore, Style

# *** INGRESO DE VARIABLES ***
# cuantas columnas necesitas?
div_x = 8
# cuantas filas necesitas?
div_y = 5
# ubicacion de la imagen?
path_big_imagen = "DHL.jpg"
# ubicacion de carpeta de selfies
path_selfie_imagen = "/home/lenin/Documentos/mosaicopy/ftpalbum/"
# nivel de transparencia (0 muy transparente, 255 nada de transparencia)
transparencia = 60
# nivel de contraste (1: imagen sin cambios, <1: reduce el contraste, >1: aumenta el contraste)
factor_contraste = 0.8

# abrir imagen para obtener sus dimensiones
pri_img, dim_x, dim_y = pri_imagen.abrir_imagen(path_big_imagen)

# procesar imagen, realizar subdivisiones, obtener coordendas para cada selfie
cant_self, arreglo_x, arreglo_y, pos_x, pos_y = pri_imagen.posicion_imagen(dim_x, dim_y, div_x, div_y)

# procesar las selfies
arreglo_selfies = selfie_imagen.abrir_fileImagen(path_selfie_imagen, pos_x, pos_y, cant_self)

# fabricar la imagen mosaico
selfie_join = crear_mosaico.unir_imagenes(arreglo_selfies, dim_x, dim_y, arreglo_x, arreglo_y)
selfie_transparencia = crear_mosaico.agregar_transparencia(selfie_join, transparencia)
selfie_transparencia = crear_mosaico.ajustar_contraste(selfie_transparencia, factor_contraste)
imagen_final = crear_mosaico.fusion(pri_img, selfie_transparencia)
imagen_final.save('imagenfinal.png', 'png')
if imagen_final: print(Fore.MAGENTA+Back.LIGHTGREEN_EX+' IMAGEN GUARDADA '+Style.RESET_ALL)
