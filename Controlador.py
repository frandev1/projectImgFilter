# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco

"""

from Manipulador_Archivos import Manipulador_Archivos
from Filtro_de_Medianas import Filtro_de_Medianas
import numpy as np
import json
import tkinter.filedialog 


class Controlador():
    def menu_de_bienvenida(self):
        '''
        Funcion que pide el tipo de ingreso de la imagen
        no tiene parametros
        '''
        print('¡Bienvenido/a al sistema de filtracion de imagenes!')
        tipo_de_ingreso = int(input('''
        ¿Como desea ingresar la imagen?
        (1) Manualmente
        (2) Seleccionando la imagen
        '''))
        # si se quiere ingresar una imagen manualmente
        if tipo_de_ingreso == 1:
            matriz_hilera = input('Ingrese la matriz que desea filtrar: ')
            # se convierte el string en lista
            matriz_hilera = self.convertir_entrada(matriz_hilera)
            # se convierte la lista en array
            matriz_array = np.asarray(matriz_hilera)
            matriz = matriz_array.tolist()
            # se calcula las dimensiones de la imagen para luego crer la imagen filtrada
            largo = len(matriz)
            ancho = len(matriz[0])
            return self.filtrar_imagen(matriz, largo, ancho)
        # si se quiere ingresar una imagen seleccionandola
        elif tipo_de_ingreso == 2:
            print('Por favor seleccione la ruta y la imagen que desea filtrar en la siguiente ventana: ')
            # se hace llamado al archivo que implementa la interfaz grafica para seleccionar la iamgen
            manipulador_de_archivos = Manipulador_Archivos()
            imagen = manipulador_de_archivos.obtener_ruta_archivo()
            # se convierte la imagen en array
            imagen_array = np.asarray(imagen)
            matriz = imagen_array.tolist()
            # se calcula las dimensiones de la imagen para luego crer la imagen filtrada
            largo = len(matriz)
            ancho = len(matriz[0])
            return self.filtrar_imagen(matriz, largo, ancho)
        # si el usuario ingresa una opcion no disponible
        else:
            print('Por favor, seleccione una opcion disponible')
            return self.menu_de_bienvenida()

    def filtrar_imagen(self, matriz, largo, ancho):
        '''
        Funcion encargada de pedir las entradas necesarias para filtrar la imagen
        parametro matriz: matriz de la imagen a filtrar
        parametro largo: largo de la imagen
        parametro ancho: ancho de la imagen
        '''
        print('Por favor seleccione la ruta donde desea que se guarde la imagen filtrada en la siguiente ventana: ')
        # se guarda la ruta donde guardara la imagen filtrada
        ruta = tkinter.filedialog.askdirectory()
        nombre_imagen_filtrada = input('Por favor ingrese el nombre con el que desea guardar la imagen filtrada: ')
        K = input('Por favor ingrese el tamano de la ventana que desea que se utilice: ')
        # se verifica que la ventana sea un numero
        try:
            K = int(K)
        except:
            print('Tamano de ventana invalida')
            return self.menu_de_bienvenida()
        algoritmo_ordenamiento = input('''
        ¿Cual algoritmo de ordenamiento le gustaria usar para filtrar la imagen?
        (1) Seleccion 
        (2) Quick Sort 
        ''')
        # se verifica que lo ingresado sea una opcion disponible o un numero
        try:
            algoritmo_ordenamiento = int(algoritmo_ordenamiento)
        except:
            print('Por favor, seleccione una opcion disponible')
            return self.menu_de_bienvenida()
        return self.filtrar_imagen_aux(matriz, K, algoritmo_ordenamiento, largo, ancho, ruta, nombre_imagen_filtrada)
    
    def convertir_entrada(self, matriz_hilera):
        '''
        Funcion encargada de converitr la hilera en lista
        parametro matriz_hilera: valores de la matriz de tipo hilera
        retorna la matriz de tipo lista
        '''
        matriz = json.loads(matriz_hilera)
        return matriz        
    
    def filtrar_imagen_aux(self, matriz, K, algoritmo_ordenamiento, largo, ancho, ruta, nombre_imagen_filtrada):
        '''
        Funcion encargada de filtrar la imagen
        parametro matriz: matriz de la iamgen que se desea filtrar
        parametro K: tamano de la ventana
        parametro algoritmo_ordenamiento: tipo de algoritmo que se desea utilizar
        parametro largo: largo de la imagen
        parametro ancho: ancho de la imagen
        parametro ruta: ruta donde se va a guardar la imagen filtrada
        parametro nombre_imagen_filtrada: nombre del archivo de la imagen filtrada
        return imagen filtrada
        '''
        # se crea la imagen filtrada con ceros y con su debido tamano
        matriz_imagen_filtrada = np.zeros((largo, ancho))
        # se llama a la clase encargada de realizar el filtrado
        filtro_de_medianas = Filtro_de_Medianas()
        matriz_imagen_filtrada = filtro_de_medianas.recorrer_imagen(matriz, K, algoritmo_ordenamiento, matriz_imagen_filtrada)
        return self.convertir_matriz_y_guardar_imagen(matriz_imagen_filtrada, ruta, nombre_imagen_filtrada)
        
    def convertir_matriz_y_guardar_imagen(self, matriz_imagen_filtrada, ruta, nombre_imagen_filtrada):
        '''
        Funcion encargada de convertir la matriz de la imagen filtrada a una imagen y guardarla
        parametro matriz_imagen_filtrada: matriz de la imagen ya filtrada
        parametro nombre_imagen_filtrada: nombre del archivo de la imagen filtrada
        parametro ruta: ruta donde se desea guardar la imagen filtrada
        '''
        manipulador_de_archivos = Manipulador_Archivos()
        manipulador_de_archivos.guardar_ruta(matriz_imagen_filtrada, ruta, nombre_imagen_filtrada)
        
        
def filtrar():    
    controlador = Controlador()
    controlador.menu_de_bienvenida()
    
filtrar()

# pruebas futuras:
# matriz_3 = np.array([[221.0, 222, 250, 251, 223, 249], [223.0, 220, 250, 251, 225, 242], [221.0, 0, 250, 251, 221, 249], [221.0, 222, 255, 251, 0, 249], [220.0, 219, 250, 251, 221, 249], [221.0, 222, 250, 251, 223, 249]])    
# ventana 3, 5, 3
# seleccion, quicksort, quicksort

# man noisy
# ventana 3, 3, 11
# seleccion, quicksort, quicksort
