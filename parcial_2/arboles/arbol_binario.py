from cola.cola import Cola

class Arbol(object):
    def __init__(self, info=None, frecuencia=None, datos=None):
        self.info = info
        self.frecuencia = frecuencia
        self.der = None
        self.izq = None
        self._altura = 0
        self.datos = datos


    def insertar_nodo(self, dato, datos=None):
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos=datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos=datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def remplazar(self):
        aux = None
        if(self.der is None):
            aux = self.info
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
            else:
                self.info = None
        else:
            aux = self.der.remplazar()
        return aux

    def eliminar_nodo(self, clave):
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos



    def inorden(self):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden()
            print(self.info)
            if(self.der is not None):
                self.der.inorden()

    def posorden(self):
        if (self.info is not None):
            if (self.der is not None):
                self.der.inorden()
            print(self.info)
            if (self.izq is not None):
                self.izq.inorden()

    def preorden(self):
        if (self.info is not None):
            print(self.info, self._altura)
            if (self.izq is not None):
                #print('izq de ', self.info)
                self.izq.preorden()
            if (self.der is not None):
                #print('der de ', self.info)
                self.der.preorden()

    def busqueda(self, clave):
        pos = None
        if (self.info is not None):
            if(self.info == clave):
                pos = self
            elif (clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif (self.der is not None):
                pos = self.der.busqueda(clave)
        return pos


    def contar_ocurrencias(self, buscado):
        cantidad = 0
        if (self.info is not None):
            if (self.info == buscado):
                cantidad += 1
            if (self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if (self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad

    def barrido_por_nivel(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)

    def barrido_por_nivel_huffman(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.frecuencia)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)

    # arbol avl
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura(self):
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1

    def rotacion_simple(self, control):
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura()
        aux.actualizar_altura()
        return aux

    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def remplazar_proximidad_MCU(self, clave, remplazar):
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.remplazar_proximidad_MCU(clave, remplazar)
            if (self.info[0:len(clave)] == clave):
                self.info = remplazar
                self.datos['nombre'] = remplazar
            if (self.der is not None):
                self.der.remplazar_proximidad_MCU(clave, remplazar)



# arbol = Arbol()
#
# arbol.insertar_nodo('F')
# arbol.insertar_nodo('B')
# arbol.insertar_nodo('E')
# arbol.insertar_nodo('C')
# arbol.insertar_nodo('B')
# arbol.insertar_nodo('K')
# arbol.insertar_nodo('R')
# arbol.insertar_nodo('H')
# arbol.insertar_nodo('J')
# arbol.insertar_nodo('A')



# print(arbol.info, arbol.izq.info, arbol.der.info)
# print('inorden')
# arbol.inorden()
# print('posorden')
# arbol.posorden()
# print('preorden')
# arbol.preorden()
# print('ELIMINAR')
# x = arbol.eliminar_nodo('A')
# print(x)
# print('barrido')
# arbol.preorden()
#
# print('BUSQUEDA')
# pos = arbol.busqueda('F')
# if pos:
#     print('elemento encontroado', pos.info)
#
# print()
# print('Barrido')
# arbol.inorden()

'''Probando arbol AVL'''


from random import randint


# PROBANDO ROTACION SIMPLE
# for i in range(3,0,-1):
#     arbol.insertar_nodo(i)
# arbol.preorden()
# arbol = arbol.rotancion_simple(True)
# print('>>>')
# arbol.preorden()

# PROBANDO ROTACION DOBLE
# arbol.insertar_nodo(3)
# arbol.insertar_nodo(1)
# arbol.insertar_nodo(2)
# arbol.preorden()
# print()
# arbol = arbol.rotacion_doble(True)
# arbol.preorden()

#PROBANDO EL BALANSEAR
# arbol = Arbol()
# for i in range(12):
#     arbol = arbol.insertar_nodo(i+1)



# arbol = arbol.insertar_nodo(1)
# arbol = arbol.insertar_nodo(3)
# arbol = arbol.insertar_nodo(2)

# print('>>>')
# arbol.preorden()
# print('>>>')
# arbol = arbol.balancear()
# arbol.preorden()

# 2,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,


















