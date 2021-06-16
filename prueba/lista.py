def __criterio(dato, criterio):
    if(criterio == None):
        return dato
    else:
        return dato[criterio]

def quicksort(vector, inicio, fin, criterio):
    primero = inicio
    ultimo = fin - 1
    pivote = fin
    while (primero < ultimo):
        while (__criterio(vector[primero], criterio) <= __criterio(vector[pivote], criterio) and primero <= ultimo):
            primero += 1
        while (__criterio(vector[ultimo], criterio) > __criterio(vector[pivote], criterio) and ultimo >= primero):
            ultimo -= 1

        if (primero < ultimo):
            vector[primero], vector[ultimo] = vector[ultimo], vector[primero]
    if (__criterio(vector[pivote], criterio) < __criterio(vector[primero], criterio)):
        vector[primero], vector[pivote] = vector[pivote], vector[primero]

    if (inicio < primero):
        quicksort(vector, inicio, primero - 1, criterio)
    if (fin > primero):
        quicksort(vector, primero + 1, fin, criterio)


class Lista(object):
    def __init__(self):
        self.__elementos = []

    def __criterio(self, dato, criterio):
        if (criterio == None):
            return dato
        else:
            return dato[criterio]



    def insertar(self, dato, criterio=None):  # tener en cuenta que la insersion debe ser ordenada
        if (len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif (self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while (pos < len(self.__elementos) and self.__criterio(dato, criterio) >= self.__criterio(
                    self.__elementos[pos], criterio)):
                pos += 1
            self.__elementos.insert(pos, dato)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)

    def barrido_lista_autos(self):
        for elemento in self.__elementos:
            print(elemento)
            print('autos: ')
            elemento['autos'].barrido()

    def lista_vacia(self):
        return len(self.__elementos) == 0

    def tamanio(self):
        return len(self.__elementos)

    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) - 1
        while (primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if (self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif (self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio - 1
            else:
                primero = medio + 1

        if (pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while (self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos - 1],
                                                                                       criterio)):
                pos -= 1

            while (self.__elementos[pos][criterio_clave] != clave and
                   self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos + 1],
                                                                                       criterio)):
                pos += 1

            if (self.__elementos[pos][criterio_clave] != clave):
                pos = -1

        return pos

    def obtener_elemento(self, pos):
        if (pos >= 0):
            return self.__elementos[pos]
        else:
            return None

    def modificar(self, pos, nuevo_valor):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor)

    def ordenar(self, criterio):
        pass

    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if (pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None

    def barrido_eliminando(self, dato_eliminar):
        for elemento in self.__elementos:
            if (elemento in dato_eliminar):
                self.__elementos.remove(elemento)




from random import randint

# lista_personas = Lista()
# lista_num = Lista()
#
# datos = [{'name': 'juan', 'edad': 34, 'provincia': 'misiones', 'dni': 32},
#          {'name': 'juan', 'edad': 80, 'provincia': 'misiones', 'dni': 52},
#          {'name': 'maria', 'edad': 56, 'provincia': 'entre rios', 'dni': 36},
#          {'name': 'julieta', 'edad': 18, 'provincia': 'catamarca', 'dni': 84},
#          {'name': 'carlos', 'edad': 40, 'provincia': 'entre rios', 'dni': 21},
#          ]

# for i in range(0, 10):
#     lista_num.insertar(randint(0, 100))
# print()
# lista_num.barrido()
#
# numero = int(input("Ingrese un valor a buscar: "))
# print(lista_num.busqueda(numero))

#
# for personas in datos:
#     lista_personas.insertar(personas, 'edad')
#
# lista_personas.barrido()
# print()
# pos = lista_personas.busqueda(18, 'edad', 'catamarca', 'provincia')
# print(pos)
# print(lista_personas.obtener_elemento(pos))
# print(lista_personas.busqueda('juan', 'name', 32, 'dni'))
