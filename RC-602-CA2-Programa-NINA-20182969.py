#importar librarias para medir la memoria usada
from __future__ import print_function
import psutil
#importar libreria para medir el tiempo de ejecucion
import time
start_time = time.time()
#importar libreria priority queque para ordenar facilmente
#los vertices que aun no se han visitado permitiendonos
#elegir el de menor costo actual
from queue import PriorityQueue
#inciciar clase Grafo
class Grafo:
    #constructor que recibe el numero de vertices
    def __init__(self, num_de_vertices):
        self.v = num_de_vertices 
        #crear matriz segun el numero de vertices
        self.edges = [[-1 for i in range(num_de_vertices)] for j in range(num_de_vertices)] 
        self.visitado = []
    #funcion agregar arista que recibe el peso, u y v
    def agregar_edge(self, u, v, peso):
        #agregar el peso a los nodos correspondientes
        self.edges[u][v] = peso
        self.edges[v][u] = peso
    #funcion del algortimo dijkstra que recibe el inicio del vertice    
    def dijkstra(self, inicio_vertice):
        #crear lista infinita
        D = {v:float('inf') for v in range(self.v)}
        #indicar que el inico del vertice es 0
        D[inicio_vertice] = 0
        pq = PriorityQueue()
        #agregar el inicio del vertice en pq
        pq.put((0, inicio_vertice))
        
        print("------------------------------------TABLA-----------------------------------")
        while not pq.empty():
            #marcar como visitado el vertice actual
            (dist, vertice_actual) = pq.get()
            self.visitado.append(vertice_actual)

            for vecino in range(self.v):
                #si la distancia de vertice actual y vecino diferente a -1
                if self.edges[vertice_actual][vecino] != -1:
                    #igualar distancia a la del vertice actual y vecino
                    distancia = self.edges[vertice_actual][vecino]
                    #si vecino no esta visitado
                    if vecino not in self.visitado:
                        #asignar a nuevo costo el peso de el inicio del vertice hasta el vecino
                        viejo_costo = D[vecino]
                        #asignar la suma del camino mas corto desde el inicio del vertice hasta el vertice actual
                        #y la distacia entre el vertice actual y el vecino
                        nuevo_costo = D[vertice_actual] + distancia
                        #Imprimir tabla con el vertice actual, el vecino actual, el peso y el costo desde nodo 0
                        print("vertice: ",vertice_actual,"|| vecino: ", vecino,"||peso: ", distancia, " ||costo desde 0:", nuevo_costo, )
                        #si el nuevo costo es menor al viejo
                        if nuevo_costo < viejo_costo:
                            #Agregar el vecino y el costo en pq
                            pq.put((nuevo_costo,vecino))
                            #Actualizar lista D con el nuevo costo
                            D[vecino] = nuevo_costo
        
        return D
#complejidad baja
'''g = Grafo(7) 
g.agregar_edge(0, 1, 2)
g.agregar_edge(0, 6, 3)
g.agregar_edge(1, 2, 4)
g.agregar_edge(2, 6, 8)
g.agregar_edge(2, 3, 6)
g.agregar_edge(3, 5, 3)
g.agregar_edge(3, 4, 6)
g.agregar_edge(4, 5, 5)
g.agregar_edge(5, 6, 1)''' 
#indicar que al grafo la cantidad de nodos 
g = Grafo(12) 
g.agregar_edge(0, 11, 5)
g.agregar_edge(0, 1, 4)
g.agregar_edge(1, 10, 8)
g.agregar_edge(1, 2, 3)
g.agregar_edge(2, 3, 5)
g.agregar_edge(3, 10, 7)
g.agregar_edge(3, 4, 3)
g.agregar_edge(4, 7, 9)
g.agregar_edge(4, 5, 2)
g.agregar_edge(5, 6, 4)
g.agregar_edge(6, 9, 10)
g.agregar_edge(6, 7, 5)
g.agregar_edge(7, 8, 1)
g.agregar_edge(8, 9, 2)
g.agregar_edge(9, 10, 2)
g.agregar_edge(10, 11, 3)

#indicar que este grafo agregado comienza en cero
D = g.dijkstra(0)
#imprimir la distancia desde 0 hasta el nodo indicado y el camino más corto
print("-------------------------DISTANCIA MÁS CORTA POR DIJKSTRA--------------------")
for vertice in range(len(D)):
    print("Distancia de nodo 0 a nodo", vertice, "es", D[vertice])
   

#medir memoria en cpu y memoria virtual
print("---------------------------------RECURSOS USADOS------------------------------")
print("Porcentaje de cpu utilizada: ",psutil.cpu_percent())    
print("Memoria fisica usada: ", psutil.virtual_memory())  # physical memory usage
print('Memoria % usada:', psutil.virtual_memory()[2])
#medir el tiempo de ejecucion de todo el programa
print("Tiempo de ejecucion de todo el programa", "--- %s segundos ---" % (time.time() - start_time))
