# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco
"""

import sys
import numpy as np
from Ordenador_Seleccion import Algoritmo_Ordenamiento_Seleccion
from Ordenador_Quick_Sort import Algoritmo_Ordenamiento_Quick_Sort
import time

class Filtro_de_Medianas:
    def recorrer_imagen(self, matriz, K, algoritmo_ordenamiento, matriz_imagen_filtrada):
        '''
        Funcion encargada de reccore cada pizel de la imagen
        parametro matriz: valores de la imagen a filtrar en una matriz
        parametro K: tamano deseado por el usuario de la ventana que recorrera la imagen
        parametro algoritmo_ordenamiento: tipo de algoritmo que se desea utilizar
        parametro matriz_imagen_filtrada: variable que contiene los valores de la imagen filtrada
        '''
        # se crea el contador de milisegundos
        contador = lambda: int(time.time() * 1000)
        # se empieza el contador
        milisegundos = contador()
        # se crea una copia de la matriz original
        matriz_copia = matriz.copy()
        # se utiliza la funcion pad de numpy para bordear la imagen con ceros
        matriz_copia = np.pad(matriz_copia, pad_width = 1)
        # limite izquierdo de la fila en la ventana y lleva el contador de la cantidad de filas
        fila = 0
        # limite derecho de la fila en la ventana
        fila_2 = K
        # limite derecho de la columna en la ventana
        columna_2 = K
        return self.recorrer_filas(matriz_copia, fila, fila_2, columna_2, algoritmo_ordenamiento, matriz_imagen_filtrada, milisegundos)

    def construir_imagen_filtrada(self, fila_filtrada, matriz_imagen_filtrada, fila):
        '''
        Funcion encargada de construir la imagen ya filtrada
        parametro fila_filtrada: fila que ya se filtro
        parametro matriz_imagen_filtrada: variable con los valores de la imagen filtrada
        parametro fila: numero de fila actual
        return imagen filtrada
        '''
        # se le suma los valores filtrados a la fila especifica 
        matriz_imagen_filtrada[fila] += fila_filtrada
        return matriz_imagen_filtrada

    def recorrer_filas(self, matriz, fila, fila_2, columna_2, algoritmo_ordenamiento, matriz_imagen_filtrada, milisegundos):
        '''
        Funcion que recorre las filas de la imagen
        parametro matriz: matriz de la imagen que se desea filtrar
        parametro fila: limite izquierdo de la fila en la ventana y lleva el contador de la cantidad de filas
        parametro fila_2: limite derecho de la fila en la ventana
        parametro columna_2: limite derecho de la columna en la ventana
        parametro algoritmo_ordenamiento: tipo de ordenamiento seleccionado por el usuario
        parametro matriz_imagen_filtrada: variable que contiene los valores de la imagen filtrada
        parametro milisegundos: contador en milisegundos de la ejecucion del filtrado
        return imagen filtrada
        '''
        #cambia el limite de la pila
        sys.setrecursionlimit(10**9)
        # si se llega a la ultima fila se detiene
        if fila == (len(matriz) -2):  # menos dos porque se eliminan los 0 del padding
        # se le informa al usuario del tiempo en milisegundos que duro el filtrado    
            print('Tiempo de ejecucion del filtrado en milisegundos:', milisegundos)
            return matriz_imagen_filtrada
        # si quedan filas por recorrer
        else:
            # limite izquierdo de la columna en la ventana y lleva la poiscion de la columna en la fila
            columna = 0
            # se crea la variable que contiene la fila ya filtrada
            fila_filtrada = []
            # se recorre cada columna de la fila, en donde se crea la ventana y se saca la mediana de todas las columna de la fila
            fila_filtrada = self.recorrer_columnas(matriz, fila, fila_2, columna, columna_2, fila_filtrada, algoritmo_ordenamiento)
            # con la fila ya filtrada se va a ir creando la imagen
            matriz_imagen_filtrada = self.construir_imagen_filtrada(fila_filtrada, matriz_imagen_filtrada, fila)
            # se sigue con la siguiente fila
            return self.recorrer_filas(matriz, fila + 1, fila_2 + 1, columna_2, algoritmo_ordenamiento, matriz_imagen_filtrada, milisegundos) # se suma uno a las filas para seguir con la siguiente
    
    def tipo_ordenamiento(self, algoritmo_ordenamiento, ventana_vectorizada):
        '''
        Funcion encargada de hacer el llamado al tipo de algoritmo de ordenamiento correspondiente
        parametro algoritmo_ordenamiento: tipo de algoritmo de ordenamiento seleccionado por el usuario
        parametro ventana_vectorizada: variable con los valores de la ventana
        return lista_ordenada
        '''
        # si el usuario escogio algorimo de seleccion
        if algoritmo_ordenamiento == 1:
            seleccion = Algoritmo_Ordenamiento_Seleccion()
            lista_ordenada = seleccion.ordenamiento_por_seleccion(ventana_vectorizada, 0)
            return lista_ordenada
        # si el usuario escogio algorimo de quick sort
        elif algoritmo_ordenamiento == 2:
            rapido = Algoritmo_Ordenamiento_Quick_Sort()
            lista_ordenada = rapido.quick_sort(ventana_vectorizada)
            return lista_ordenada
        
    def calcular_mediana_ventana(self, lista_ordenada):
        '''
        Funcion encargada de calcular la mediana de una lista
        parametro lista_ordenada: lista que se desea averiguar su mediana
        return: el valor de la mediana
        '''
        mediana = ((len(lista_ordenada) + 1) // 2) -1
        valor_mediana = lista_ordenada[mediana]
        return valor_mediana   
     
    def recorrer_columnas(self, matriz, fila, fila_2, columna, columna_2, fila_filtrada, algoritmo_ordenamiento):
        '''
        Funcion encargada de recorrer las columnas de la fila
        parametro matriz: matriz de la imagen que se desea filtrar
        parametro fila: limite izquierdo de la fila en la ventana y lleva el contador de la cantidad de filas
        parametro fila_2: limite derecho de la fila en la ventana
        parametro columna: limite izquierdo de la columna en la ventana y lleva la poiscion de la columna en la fila
        parametro columna_2: limite derecho de la columna en la ventana
        parametro fila_filtrada: variable que contiene la fila ya filtrada
        parametro algoritmo_ordenamiento: tipo de ordenamiento seleccionado por el usuario
        return fila ya filtrada
        '''
        #cambia el limite de la pila
        sys.setrecursionlimit(10**9)
        # si se llega a la ultima columna, entonces se retorna la fila filtrada
        if columna == (len(matriz[0]) -2): # se le restan los ceros agregados en el padding
            return fila_filtrada
        # si quedan columnas restantes
        else:
            # se crea la ventana con slicing de las filas y columnas
            ventana = matriz[fila : fila_2, columna : columna_2]
            # se vectoriza la ventana
            ventana_vectorizada = ventana.flatten()
            lista_ordenada = self.tipo_ordenamiento(algoritmo_ordenamiento, ventana_vectorizada)
            # se calcula la mediana de la ventana ordenada
            mediana = self.calcular_mediana_ventana(lista_ordenada)
            # se agrega la mediana a la lista de la fila filtrada
            fila_filtrada += [mediana]
            # se sigue con la siguiente columna
            return self.recorrer_columnas(matriz, fila, fila_2, columna + 1, columna_2 + 1, fila_filtrada, algoritmo_ordenamiento)
   