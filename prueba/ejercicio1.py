#  Dado un vector con personaje de las películas de la saga de Star Wars resolver las
# siguientes actividades:
#  a. Realizar un barrido recursivo del vector.
#  b. Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
# vector y en que posición

personajes = ['Darth Vader', 'Yoda', 'Chewbacca', 'R2-D2', 'Obi-Wan Kenobi', 'Anakin Skywalker', 'Luke Skywalker']


def barrido(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[-1] + "\n" + barrido(lista[0:-1])

resultado = barrido(personajes)
print(resultado)





