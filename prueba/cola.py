class Cola(object):
    def __init__(self):
        self.__elementos = []

    def arribo(self, dato):  # agrega un elemento al final de la cola
        self.__elementos.append(dato)

    def atencion(self):  # elimina y devuelve el elemento almacenado en el frente de la cola
        return self.__elementos.pop(0)

    def cola_vacia(self):  # devuelve verdadero si la cola no contiene elementos
        return len(self.__elementos) == 0

    def en_frente(self):  # devuelve el valor del elemento que está almacenado en el frente de la cola sin eliminarlo
        return self.__elementos[0]

    def mover_al_final(self): # elimina el elemento en el frente de la cola y lo inserta en el final de la misma
        dato = self.atencion()
        self.arribo(dato)
        return dato

    def tamanio(self):
        return len(self.__elementos)