# -*- coding: utf-8 -*-
"""
@autores: Dayana, Abel, Franco
"""

class Algoritmo_Ordenamiento_Seleccion:
    
    def encontrar_numero_menor(self, lista_a_ordenar, numero_menor, posicion, posicion_numero_menor):
        '''
        Funcion encargada de encontrar el numero menor y su posicion de la lista a ordernar
        parametro lista_a_ordenar: lista que se desea ordenar 
        parametro numero_menor: variable que guarda el numero menor
        parametro posicion: numero de posicion a indexar la lista
        parametro posicion_numero_menor: variable que guarda la posicion del numero menor de la lista
        return: la posicion y el valor del numero menor

        '''
        # si la posicion ya termino de recorrer toda la lista
        if posicion == len(lista_a_ordenar):
            return (posicion_numero_menor, numero_menor)
        else:
            # si el numero actual de la lista es mayor que el numero_menor
            if numero_menor < lista_a_ordenar[posicion]:
                # se sigue con el siguiente numero en la lista
                posicion += 1
                return self.encontrar_numero_menor(lista_a_ordenar, numero_menor, posicion, posicion_numero_menor)
            # si el numero actual de la lista es menor que el numero_menor
            else:
                # actualizar la variable con el nuevo numero menor
                numero_menor = lista_a_ordenar[posicion]
                # guardar la posicion del numero menor encontrado
                posicion_numero_menor = posicion
                # se sigue revisando los numeros restantes de la lista
                posicion += 1
                return self.encontrar_numero_menor(lista_a_ordenar, numero_menor, posicion, posicion_numero_menor)

    def intercambiar(self, posicion_1, posicion_2, lista):
        """
        Intercambia los valores en la lista lista, en posicion_1  y posicion_2
        param posicion_1: primer posicion a intercambiar
        param posicion_2: segunda posicion a intercambiar
        return: lista con los elementos intercambiados
        """
        # se realiza el intercambio de valores con sus posiciones
        variable_temporal = lista[posicion_1]
        lista[posicion_1] = lista[posicion_2]
        lista[posicion_2] = variable_temporal
        return lista

    def ordenamiento_por_seleccion(self, lista_a_ordenar, pivote): 
        '''
        Funcion que aplica el algoritmo de ordenamiento por seleccion con recursividad de pila
        parametro lista_a_ordenar: lista que se desea ordenar 
        parametro pivote: posicion actual que se esta leyendo en al lista
        parametro contador: variable que cuenta las veces que se mueve el pivote
        return: lista ya ordenada
        '''
        # se crea una copia de la lista original para no modificar la original
        lista_a_ordenar_copia = lista_a_ordenar.copy()
        largo_lista = len(lista_a_ordenar_copia) 
        # condicion de parada, si el pivote llego al ultimo elemento
        if(pivote == largo_lista -1):
            # se retorna el ultimo elemento
            return [lista_a_ordenar_copia[pivote]]
        else: 
            # se busca la posicion y el valor del numero menor en la lista y se revisan solo los numeros que estan despues del pivote
            (posicion_numero_menor, numero_menor) = self.encontrar_numero_menor(lista_a_ordenar_copia[pivote :], lista_a_ordenar_copia[pivote], 0, 0) # se inicializa en cero las posiciones
            # se le suma a la posicion el pivote, esto para sumar los numeros que estan antes del pivote que no se revisaron
            posicion_numero_menor += pivote
            # se hace el intercambio de valores en la lista
            lista_a_ordenar_copia = self.intercambiar(pivote, posicion_numero_menor, lista_a_ordenar_copia)
            # se suma uno al pivote para seguir ordenando
            pivote += 1
            return [numero_menor] + self.ordenamiento_por_seleccion(lista_a_ordenar_copia, pivote)