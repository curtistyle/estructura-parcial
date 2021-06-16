

# Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone, de las cual se cuenta
# con la hora de la notificación, la aplicación que la emitió y el
# mensaje, resolver las siguientes actividades:
#     c. escribir una función que elimine de la cola todas las notificaciones de
#     Facebook;
#     d. escribir una función que muestre todas las notificaciones de Twitter, cuyo
#     mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#     e. utilizar una pila para almacenar temporalmente las notificaciones de
#     Instagram y mostrar el contenido de dicha pila.

from cola import Cola
from pila import Pila

class Notificacion(object):
    def __init__(self, h=None, a=None ,m=None):
        self.__hora = h
        self.__aplicacion = a
        self.__mensaje = m

    def obtener_hora(self):
        return self.__hora

    def obtener_aplicacion(self):
        return self.__aplicacion

    def obtener_mensaje(self):
        return self.__mensaje



# def eliminar_facebook(cola : Cola):
#     dato = Notificacion()
#     cola_aux = Cola()
#     while not cola.cola_vacia():
#         dato = cola.atencion()
#         if dato.obtener_aplicacion() != 'Facebook':
#             cola_aux.arribo(dato)
#     return cola_aux

def eliminar_facebook(notificacion : Notificacion):
    if notificacion.obtener_aplicacion() != 'Facebook':
        return True
    else:
        return False

def mostrar_python(notificacion : Notificacion):
    if notificacion.obtener_aplicacion() == 'Twitter' and 'Python' in notificacion.obtener_mensaje():
        print('Notificacion de Twitter: ')
        print()
        print(notificacion.obtener_mensaje())


cola_notificaciones = Cola()
cola_aux = Cola()
notificacion = Notificacion()

vec = [
        Notificacion('15:30', 'Facebook', 'Pasame a buscar'),
        Notificacion('18:00', 'Facebook', 'Mañana'),
        Notificacion('01:00', 'Twitter', 'Estoy programando en Python'),
        Notificacion('22:30', 'WhatsApp', 'Mas Tarde'),
        Notificacion('00:00', 'Instagram', 'La semana que viene es feriado'),
        Notificacion('00:30', 'Instagram', 'Lunes')
       ]

for notificacion in vec:
    cola_notificaciones.arribo(notificacion)
# C)- escribir una función que elimine de la cola todas las notificaciones de Facebook;
while not cola_notificaciones.cola_vacia():
    aux = cola_notificaciones.atencion()
    if eliminar_facebook(aux) == True:
        cola_aux.arribo(aux)

while not cola_aux.cola_vacia():
    cola_notificaciones.arribo(cola_aux.atencion())

cantidad_de_elementos = 0
while cantidad_de_elementos < cola_notificaciones.tamanio():
    notificacion = cola_notificaciones.mover_al_final()
    print(notificacion.obtener_aplicacion())
    cantidad_de_elementos += 1

# D)- escribir una función que muestre todas las notificaciones de Twitter, cuyo
# mensaje incluya la palabra ‘Python’, si perder datos en la cola;
while not cola_notificaciones.cola_vacia():
    aux = cola_notificaciones.atencion()
    mostrar_python(aux)
    cola_aux.arribo(aux)

while not cola_aux.cola_vacia():
    cola_notificaciones.arribo(cola_aux.atencion())



# E)- utilizar una pila para almacenar temporalmente las notificaciones de
# Instagram
pila = Pila()

cantidad_de_elementos = 0
while cantidad_de_elementos < cola_notificaciones.tamanio():
    notificacion = cola_notificaciones.mover_al_final()
    print(notificacion.obtener_aplicacion())
    cantidad_de_elementos += 1

while not cola_notificaciones.cola_vacia():
    notificacion = cola_notificaciones.atencion()
    if 'Instagram' in notificacion.obtener_aplicacion():
        pila.apilar(notificacion)

while not pila.pila_vacia():
    notificacion = pila.desapilar()
    print('Hora: ' + notificacion.obtener_hora() + '/ Aplicacion: ' + notificacion.obtener_aplicacion() + '/ Mensaje: ' + notificacion.obtener_mensaje())



# cola_aux = eliminar_facebook(cola_notificaciones)
#
# cantidad_de_elementos = 0
# while cantidad_de_elementos < cola_aux.tamanio():
#     notificacion = cola_aux.mover_al_final()
#     print(notificacion.obtener_aplicacion())
#     cantidad_de_elementos += 1
#
# cola_aux = mostrar_python(cola_notificaciones)
#
# cantidad_de_elementos = 0
#
# while cantidad_de_elementos < cola_aux.tamanio():
#     notificacion = cola_aux.mover_al_final()
#     print(notificacion.obtener_aplicacion())
#     cantidad_de_elementos += 1
#






