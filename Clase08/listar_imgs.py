import sys
import os

def esPNG(name):
    return name[-4:].lower() == '.png' 

def archivos_png(directorio):
    '''
    Crea un array con los nombres de todos los archivos .png.-
    Pre: el directorio no puede estar vacío.-

    Parameters
    ----------
    directorio : TYPE string
        DESCRIPTION. directorio raíz

    Returns
    -------
    archivos : TYPE array
        DESCRIPTION. array de nombres de archivos .png

    '''
    nombre_archivos = []
    for root, dirs, files in os.walk(directorio):
        for nombre in files:
            if esPNG(nombre):
                nombre_archivos.append(nombre)

    return nombre_archivos

if __name__ == '__main__':
    if len(sys.argv) == 2:
        directorio = sys.argv[1]
        names = archivos_png(directorio)
        print(names)
