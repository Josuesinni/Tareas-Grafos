from Nodo import Nodo
from Arco import Arco
from Grafo import Grafo

#archivo = open('data/scc.txt')
#archivo = open('data/ord_topologico.txt')
#archivo = open('data/esparcimiento_minimo.txt')
#archivo = open('data/Ordenamiento Topológico/Ejemplo2.txt')
#archivo = open('data/Coponentes Fuertemente Conectados/Ejemplo2.txt')
#archivo = open('data/Kruskal/Ejemplo2.txt')
archivo = open('data/Prim/Ejemplo2.txt')
lineas = archivo.readlines()
nodos = {}
arcos = []
grafo = Grafo ("Grafo")
for linea in lineas:
    elemento = linea.split()
    if len(elemento) == 2:
        nodos[elemento[0]]=(Nodo(elemento[0]))
        nodos[elemento[1]]=(Nodo(elemento[1]))
        arcos.append(Arco(elemento[0],elemento[1],float(1)))
    elif len(elemento) == 3:
        nodos[elemento[0]]=(Nodo(elemento[0]))
        nodos[elemento[1]]=(Nodo(elemento[1]))
        arcos.append(Arco(elemento[0],elemento[1],float(elemento[2])))
    elif len(elemento)== 1:
        nodos[elemento[0]]=(Nodo(elemento[0]))
for nodo in nodos:
    grafo.addNodo(nodo)
    
for arco in arcos:
    grafo.addArco(arco)

#Establecer el punto de inicio de un grafo BFS
#grafo.bfs("a")
#grafo.graficar()

#Ordenar por tiempo los nodos metodo dfs
"""
print(grafo)
grafo.dfs()
#print(grafo)
#grafo.graficar()
#Se usan los grafos de forma decreciente
lista = sorted(grafo.getV(), key=lambda tupla:tupla[1], reverse= True)
newList=[]
for element in lista:
    newList.append(element[0])
#"""

#print(grafo)
#Componentes fuertemente conectados SCC
"""
gt = grafo.getTranspuesto()
gt.dfs()
bosque=gt.scc(newList)
for arbol in bosque:
    print(f"{[nodo.nombre for nodo in arbol]}")
#"""
#Ordenamiento topologico
"""
print(grafo)
grafo.dfs()
lista=grafo.get_lista()
print(f"{[(element.nombre) for element in lista]}")
#for element in lista:
#    print(element)
#"""
"""    
#Algoritmo Kruskal
print(grafo)
kruskal=grafo.mst_kruskal()
print(kruskal)
#kruskal.graficar()
#"""
#"""
print(grafo)
prim=grafo.mst_prim("s")
print(prim)
prim.graficar()
#"""

