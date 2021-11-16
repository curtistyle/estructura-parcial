from arboles.arbol_binario import Arbol

dic = [ {'nombre': 'Arctodus',       'codigo': 34233, 'zona': 'A1'},
        {'nombre': 'Diplodocus',     'codigo': 76535, 'zona': 'E1'},
        {'nombre': 'Gigantoraptor',  'codigo': 65271, 'zona': 'E1'},
        {'nombre': 'Raptor',         'codigo': 99981, 'zona': 'U1'},
        {'nombre': 'Carbonemys',     'codigo': 13467, 'zona': 'I1'},
        {'nombre': 'Sgimoloch',      'codigo': 13467, 'zona': 'I1'},
        {'nombre': 'Raptor',         'codigo': 98561, 'zona': 'A2'},
        {'nombre': 'Diabloceratops', 'codigo': 98723, 'zona': 'O1'},
        {'nombre': 'T-Rex',          'codigo': 43443, 'zona': 'U1'},
        {'nombre': 'Fukuisaurus',    'codigo': 98383, 'zona': 'A2'},
        {'nombre': 'Raptor',         'codigo': 87823, 'zona': 'A2'},
        {'nombre': 'Henodus',        'codigo': 33341, 'zona': 'E2'},
        {'nombre': 'Diplodocus',     'codigo': 11111, 'zona': 'A1'},
        {'nombre': 'T-Rex',          'codigo': 22331, 'zona': 'U1'},
        {'nombre': 'Raptores',       'codigo': 22113, 'zona': 'U1'},
        {'nombre': 'Kaiwhekea',      'codigo':   792, 'zona': 'I2'},
        {'nombre': 'Raptor',         'codigo': 32122, 'zona': 'I2'}
        ]

arbol_dinosaurio_nombre = Arbol()
arbol_dinosaurio_codigo = Arbol()

def informacion(arbol : Arbol, buscado):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            informacion(arbol.izq,buscado)
        if arbol.datos['nombre'] == buscado:
            print(arbol.datos)
        if (arbol.der is not None):
            informacion(arbol.der,buscado)


'''Arbol dinosaurio por nombre'''
for i in dic:
    arbol_dinosaurio_nombre = arbol_dinosaurio_nombre.insertar_nodo(i['nombre'],i)

'''Arbol dinosaurio por codigo'''
for j in dic:
    arbol_dinosaurio_codigo = arbol_dinosaurio_codigo.insertar_nodo(j['codigo'],j)

'''Barrido por nombre ordenado de los dinosaurios'''

def barrido_nombre(arbol : Arbol):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            barrido_nombre(arbol.izq)
        print(arbol.datos['nombre'])
        if (arbol.der is not None):
            barrido_nombre(arbol.der)
print('>>> Barrido del arbol por nombre: ')
barrido_nombre(arbol_dinosaurio_nombre)
print()

'''Muestra toda la informacion del dinosaurio 792'''

print('>>> Informacion del donosaurio 792')
dino = arbol_dinosaurio_codigo.busqueda(792)
print(dino.datos)
print()

'''Muestra toda la informacion de todos los T-Rex'''
print('>>> Informacion de todos los T-Rex')
informacion(arbol_dinosaurio_nombre,'T-Rex')
print()

'''Modica el nombre Sgimoloch en ambos arboles por Stygimoloch;'''

print('>>> Modifica Sgimoloch por Stygimoloch')

arbol_dinosaurio_nombre.remplazar_proximidad_MCU('Sgimoloch','Stygimoloch')

barrido_nombre(arbol_dinosaurio_nombre)
print()

'''Mostrar la ubicacion de todos los raptores'''

print('>>>Ubicacion de todos los raptores: ')
def mostrar_ubicacion(arbol : Arbol, buscado):
    if (arbol.info is not None):
        if (arbol.izq is not None):
            mostrar_ubicacion(arbol.izq,buscado)
        if arbol.datos['nombre'] == buscado:
            print('El dinosaurio: ',arbol.datos['nombre'], ' esta en la zona: ', arbol.datos['zona'])
        if (arbol.der is not None):
            mostrar_ubicacion(arbol.der,buscado)

mostrar_ubicacion(arbol_dinosaurio_nombre,'Raptor')
print()

''' Cuenta cuantos Diplodocus hay en el parque '''

print('>>> Cantidad de Diplodocus en el parque')

cantidad = arbol_dinosaurio_nombre.contar_ocurrencias('Diplodocus')

print(f'Numero de Diplodocus: {cantidad}')






