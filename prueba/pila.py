class Pila(object):

    # metodo constructor
    def __init__(self):
        self.__elementos = []  # defino una lista dinamico y lo inicializo

    def apilar(self, dato):
        self.__elementos.append(dato)  # agrego un elemento al final de la lista

    def desapilar(self):
        return self.__elementos.pop()  # devuelve el elemento de la cima de la pila

    def pila_vacia(self):
        return len(self.__elementos) == 0  # si la pila esta viacia el metodo pila_vacia devuelve true

    def tamanio(self):
        return len(self.__elementos)  # devuelce la cantidad de elementos que tiene la pila

