from grafo.grafo import Grafo


grafoRed = Grafo(dirigido = False ) #Grafo no dirigido.

grafoRed.insertar_vertice("Ubuntu", data ="PC")
grafoRed.insertar_vertice("Mint", data ="PC")

grafoRed.insertar_vertice("Impresora", data ="Impresora")

grafoRed.insertar_vertice("Switch1", data ="Switch")

grafoRed.insertar_vertice("Debian", data ="Notebook")

grafoRed.insertar_vertice("Router1", data ="Router")
grafoRed.insertar_vertice("Router2", data ="Router")
grafoRed.insertar_vertice("Router3", data ="Router")

grafoRed.insertar_vertice("Red Hat", data ="Notebook")

grafoRed.insertar_vertice("Guarani", data ="Servidor")

grafoRed.insertar_vertice("Manjaro", data ="PC")

grafoRed.insertar_vertice("Switch2", data ="Switch")

grafoRed.insertar_vertice("Fedora", data ="PC")

grafoRed.insertar_vertice("Parrot", data ="PC")

grafoRed.insertar_vertice("MongoDB", data ="Servidor")

grafoRed.insertar_vertice("Arch", data ="Notebook")

grafoRed.insertar_arista(17,"Switch1","Debian")
grafoRed.insertar_arista(18,"Switch1","Ubuntu")
grafoRed.insertar_arista(22,"Switch1","Impresora")
grafoRed.insertar_arista(80,"Switch1","Mint")
grafoRed.insertar_arista(29,"Switch1","Router1")
grafoRed.insertar_arista(37,"Router1","Router2")
grafoRed.insertar_arista(43,"Router1","Router3")

grafoRed.insertar_arista(25,"Router2","Red Hat")
grafoRed.insertar_arista(9,"Router2","Guarani")
grafoRed.insertar_arista(50,"Router2","Router3")
grafoRed.insertar_arista(61,"Router3","Switch2")
grafoRed.insertar_arista(3,"Switch2","Fedora")
grafoRed.insertar_arista(56,"Switch2","Arch")
grafoRed.insertar_arista(5,"Switch2","MongoDB")
grafoRed.insertar_arista(12,"Switch2","Parrot")
grafoRed.insertar_arista(40,"Switch2","Manjaro")

'''2_ Realiza barrido profundidad '''

print('>>> Barrido por profundidad y por amplitud')

buscado = "grafoRed Hat"
origen = grafoRed.buscar_vertice(buscado)

print("Barrido en profundidad desde grafoRed Red Hat: ")
grafoRed.barrido_profundidad(origen)
grafoRed.marcar_no_visitado()
print()

print("Barrido en amplitud desde grafoRed Red Hat:")
grafoRed.barrido_amplitud(origen)
grafoRed.marcar_no_visitado()
print()

buscado_2 = "Debian"
origen_2 = grafoRed.buscar_vertice(buscado_2)
print("Barrido en profundidad desde Debian: ")
grafoRed.barrido_profundidad(origen_2)
grafoRed.marcar_no_visitado()
print()

print("Barrido en amplitud desde Debian:")
grafoRed.barrido_amplitud(origen_2)
grafoRed.marcar_no_visitado()
print()


buscado_3 = "Arch"
origen_3 = grafoRed.buscar_vertice(buscado_3)

print("Barrido en profundidad desde Arch: ")
grafoRed.barrido_profundidad(origen_3)
grafoRed.marcar_no_visitado()
print()

print("Barrido en amplitud desde Arch:")
grafoRed.barrido_amplitud(origen_3)
grafoRed.marcar_no_visitado()
print()


'''3_ Encontrar el camino mas corto'''
buscado_1 = "Debian"
origen = grafoRed.buscar_vertice(buscado_1)
buscado_2 = "MongoDB"
destino = grafoRed.buscar_vertice(buscado_2)
camino_mas_corto = grafoRed.dijkstra(origen,destino)
print("Camino mas corto desde la pc Debian hasta el MongoDB ")
destino = buscado_2

costo = None
while(not camino_mas_corto.pila_vacia()):
    dato = camino_mas_corto.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo del camino de Debian a Mongo DB es:', costo)
print()

buscado1 = "grafoRed Hat"
origen = grafoRed.buscar_vertice(buscado1)
buscado2 = "MongoDB"
destino = grafoRed.buscar_vertice(buscado2)
camino_mas_corto = grafoRed.dijkstra(origen,destino)

destino = buscado2
costo = None
print("Camino mas corto desde la  pc grafoRed Hat hasta el MongoDB ")
while(not camino_mas_corto.pila_vacia()):
    dato = camino_mas_corto.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino desde grafoRed Hat a Mongo DB es ', costo)
print()

'''Arbol de expansion minimo'''
bosque = grafoRed.prim()
print('Arbol de expansion mínimo')

peso = 0
for elementos in bosque:
    print(elementos[1][0], '-', elementos[1][1])
    peso += elementos[0]
print('Costo total', peso)
print()

'''5_barrido profundidad'''
grafoRed.eliminar_vertice("Impresora")
origen = grafoRed.buscar_vertice("Switch1")
print("Barrido sin la impresora ")
grafoRed.barrido_profundidad(origen)