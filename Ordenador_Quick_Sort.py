# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco
"""

class Algoritmo_Ordenamiento_Quick_Sort:
    def quick_sort(self, lista):      
        '''
        Funcion encargada de realzar el ordenamiento del quick sort
        parametro lista: lista que se desea ordenar
        return lista_ordenada
        '''
        # se inicializa el pivote en el primer elemento  
        elemento_pivote = lista[0]
        # se crea la lista de los mayores
        lista_mayores = []
        # se crea la lista de los menores
        lista_menores = []
        # se recorre la lista desde el pivote hacia la derecha
        lista = lista[1:]
        # se guarda la lista de menores, el pivote y la lista de mayores
        (lista_menores, elemento_pivote, lista_mayores)  = self.crear_listas_mayores_menores(lista, elemento_pivote, lista_menores, lista_mayores)        
        # si la lista de menores no ha terminado de dividirse en sublistas
        if(len(lista_menores) > 1):
            lista_menores = self.quick_sort(lista_menores)
        # si la lista de mayores no ha terminado de dividirse en sublistas
        if(len(lista_mayores) > 1):
            lista_mayores = self.quick_sort(lista_mayores)
        # si ya se termino de ordenar se crea la lista final ordenada
        lista_ordenada = lista_menores + [elemento_pivote] + lista_mayores
        return lista_ordenada

    def crear_listas_mayores_menores(self, lista, elemento_pivote, lista_menores, lista_mayores):
        '''
        Funcion que crea las listas mayores y menores
        parametro lista: lista que se desea ordenar
        parametro elemento_pivote: primer elemento de la lista que trabaja como pivote
        parmetro lista_menores: lista de los menores elementos al pivote
        parametro lista_mayores: lista de los mayores elementos al pivote
        '''
        # si ya no quedan elementos en la lista se retorna la lista_menores, elemento_pivote y lista_mayores
        if len(lista) == 0:
            return (lista_menores, elemento_pivote, lista_mayores)
        # si el elemento actual es menor que el pivote se agrega a la lista de menores
        elif lista[0] < elemento_pivote:
            lista_menores += [lista[0]]
            # se hace el llamado recursivo
            return self.crear_listas_mayores_menores(lista[1:], elemento_pivote, lista_menores, lista_mayores)
        # si el elemento actual es mayor o igual que el pivote se agrega a la lista de menores
        else:
            lista_mayores += [lista[0]]
            # se hace el llamado recursivo
            return self.crear_listas_mayores_menores(lista[1:], elemento_pivote, lista_menores, lista_mayores)


