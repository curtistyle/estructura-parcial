from lista import Lista, quicksort

# 3. Dada una lista con nombres de personajes de la saga de Avengers, resolver las
# siguientes tareas:
#   a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
# misma;
#   b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
#   c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
# ‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
# cargados.
#   d. Realizar un barrido ascendente y descendente de la lista.
#   e. Mostrar la información del personaje en la posición 7.
#   f. Mostrar todos los personajes que comienzan con C o S.
#   g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
# booleano que indica si es héroe True villano False), luego realizar un barrido
# ordenado por nombre y otro por año de aparición. Deberá cargar toda la
# información de nuevo.

lista_personajes = Lista()

personajes = [
    {'name': 'Iron Man'},
    {'name': 'Hulk'},
    {'name': 'Black Widow'},
    {'name': 'Thor'},
    {'name': 'Hawkeye'},
    {'name': 'Capitan America'},
    {'name': 'Soldado del Invierno'},
    {'name': 'Scalet Witch'}
]

for personaje in personajes:
    lista_personajes.insertar(personaje, 'name')

# barrido
lista_personajes.barrido()


#   a. Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la
# misma.

pos = lista_personajes.busqueda('Thor', 'name')
print('Thor esta en la posicion: ', pos)

#   b. Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;

pos = lista_personajes.busqueda('Scalet Witch', 'name')
if (pos != -1):
    lista_personajes.obtener_elemento(pos)["name"] = "Scarlet Witch"

# barrido

# c. Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
#  ‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar
#   cargados.

lista_personajes.barrido()

lista_auxliar = Lista()

personajes_auxiliar = [
    {'name': 'Black Widow'},
    {'name': 'Hulk'},
    {'name': 'Rocket Racoonn'},
    {'name': 'Loki'}
]

for personaje in personajes_auxiliar:
    lista_auxliar.insertar(personaje, 'name')


for i in range(lista_auxliar.tamanio()):
    nombre = lista_auxliar.obtener_elemento(i)
    if lista_personajes.busqueda(nombre['name'], 'name') == -1:
        lista_personajes.insertar(nombre, 'name')


# barrido
print('##########  D  ##############')
lista_personajes.barrido()

# e. Mostrar la información del personaje en la posición 7.
print('##########  E  ##############')
print(lista_personajes.obtener_elemento(8))

# f. Mostrar todos los personajes que comienzan con C o S.
print('##########  F  ##############')
for i in range(lista_personajes.tamanio()):
    personaje = lista_personajes.obtener_elemento(i)
    if personaje['name'][0] in ["C", "S"]:
        print(personaje['name'])


#   g. Ahora los datos cambiaron y debe incluir (año de aparición y un campo
# booleano que indica si es héroe True villano False), luego realizar un barrido
# ordenado por nombre y otro por año de aparición. Deberá cargar toda la
# información de nuevo.
print('##########  G  ##############')

nueva_lista_personaje = Lista()

personajes2 = [
    {'name': 'Iron Man', 'anio': 1995, 'personalidad': True},
    {'name': 'Hulk', 'anio': 2005, 'personalidad': True},
    {'name': 'Black Widow', 'anio': 2014, 'personalidad': True},
    {'name': 'Thor', 'anio': 1994, 'personalidad': True},
    {'name': 'Hawkeye', 'anio': 2010, 'personalidad': False},
    {'name': 'Capitan America', 'anio': 1850, 'personalidad': True},
    {'name': 'Soldado del Invierno', 'anio': 2000, 'personalidad': False},
    {'name': 'Scalet Witch', 'anio': 2001, 'personalidad': False}
]

for personaje in personajes2:
    nueva_lista_personaje.insertar(personaje, 'name')

print('Barrido por nombre: ')
for i in range(0,nueva_lista_personaje.tamanio()):
    print(nueva_lista_personaje.obtener_elemento(i)['name'])

print('Barrido por anio: ')
quicksort(nueva_lista_personaje,0,nueva_lista_personaje.tamanio(),'anio')
for i in range(0,nueva_lista_personaje.tamanio()):
    print(nueva_lista_personaje.obtener_elemento(i)['anio'])


















