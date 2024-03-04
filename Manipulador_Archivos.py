# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco
"""

import tkinter.filedialog 
import os 
from PIL import Image
import numpy as np

class Manipulador_Archivos:
    def obtener_ruta_archivo(self):
        """
        función encargada de obtener la ruta del archivo ingresada por el usuario
        no tiene parámetros
        return: el directorio y nombre del archivo 
        """
        # elimina la ventana que trae por defecto tkinter
        raiz = tkinter.Tk()
        # cierra la ventana por defecto de tkinter
        raiz.withdraw()
        # abre un cuadro de diálogo al usuario
        ruta_archivo = tkinter.filedialog.askopenfilename()
        # se divide la ruta para obetner el nombre del archivo 
        obtener_nombre_archivo = os.path.split(ruta_archivo)
        # obtiene el nombre del archivo
        nombre_archivo = obtener_nombre_archivo[-1]
        # se le muestra al usuario el nombre del archivo seleccionado
        print('Nombre de la imagen:',nombre_archivo)
        return self.verificar_archivo_imagen(ruta_archivo)
    
    def verificar_archivo_imagen(self, ruta_archivo):
        '''
        Funcion encargada de verificar que el archivo seleccionado sea una imagen
        parametro ruta_archivo: ruta donde se encuentra la imagen
        '''
        try:
            imagen = Image.open(ruta_archivo)
            print("La imagen se cargó exitosamente")
            return imagen 
        except:
            print("El archivo seleccionado no corresponde a una imagen, por favor intente otra vez.")
            obtener_imagen = Manipulador_Archivos()
            obtener_imagen.obtener_ruta_archivo()

    def guardar_ruta(self, matriz_imagen_filtrada, ruta, nombre_imagen_filtrada):
        """
        Función encargada de almacenar el resultado del programa en una ruta seleccionado por el cliente. 
        parametro matriz_imagen_filtrada:matriz de la imagen filtrada a converir en imagen
        parametro ruta: ruta donde se quiere guardar la imagen filtrada
        parametro nombre_imagen_filtrada: nombre del archivo de la imagen filtrada
        """      
        # se le asigna al nombre ingresado el formado png
        nombre_imagen_filtrada += '.png'
        # se le agrega a la ruta la imagen filtrada
        ruta += '/' + nombre_imagen_filtrada
        # convierte la imagen en escala de grises
        guardar = (((matriz_imagen_filtrada - matriz_imagen_filtrada.min()) / (matriz_imagen_filtrada.max() - matriz_imagen_filtrada.min())) * 255.9).astype(np.uint8)
        # se convierte la matriz en imagen
        imagen_filtrada = Image.fromarray(guardar)
        # se guarda la imagen en la ruta especificada
        imagen_filtrada.save(ruta)
        print('Se ha guardado la imagen en:', ruta)



