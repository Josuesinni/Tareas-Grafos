from Nodo import Nodo, Color
from Arco import Arco
import networkx as nx
import matplotlib.pyplot as plt
class Grafo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.V = {}
        self.lista=[]
    
    def addNodo(self, nombreNodo):
        if nombreNodo not in self.V:
            self.V[nombreNodo]=Nodo(nombreNodo)
        return self.V[nombreNodo]
    
    def addArco(self, arco):
        origen = self.addNodo(arco.origen)
        destino = self.addNodo(arco.destino)
        origen.addAdyacentes(arco)
        #destino.addAdyacentes(Arco(arco.destino, arco.origen, arco.costo))
        
    def getE ( self):
        E = []
        for nodo in self.V.values():
            for arco in nodo.adyacentes.values():
                E.append(arco)
        return E

    def getV (self):
        lista = []
        for nodo in self.V.values():
            lista.append((nodo.nombre, nodo.f))
        return lista
    
    def bfs (self, nombreOrigen):
        s = self.V[nombreOrigen]
        if s is None: 
            return
        for nodo in self.V.values():
            nodo.color = Color.BLANCO
            nodo.d = float ("Inf")
            nodo.p = None
        s.color = Color.GRIS
        s.d = 0
        Q = []
        Q.append(s)
        while len(Q)>0:
            u = Q.pop(0)
            print(u)
            for ady in u.adyacentes.keys():
                #print(ady)
                v = self.addNodo(ady)
                if v.color==Color.BLANCO:
                    v.color=Color.GRIS
                    v.d = u.d+1
                    v.p = u
                    Q.append(v)
            u.color = Color.NEGRO
        print(Q)
     
    def getTranspuesto(self):
        gt = Grafo(self.nombre + "-transpuesto")
        for nodo in self.V.values():
            gt.addNodo(nodo.nombre)
            for arco in nodo.adyacentes.values():
                gt.addArco(Arco(arco.destino,arco.origen,arco.costo))
        return gt
    
    def dfs(self):
        for nodo in self.V.values():
            nodo.color = Color.BLANCO
            nodo.p = None
        tiempo = 0
        for nodo in self.V.values(): 
            #if not nodo.adyacentes:  #si el nodo no tiene adyacentes se omite (es un nodo aislado)
            #    continue 
            #Esta es la iteración, que vamos a hacer en lugar de iterar lso valores de V, vamos a iterar la lista que acabamos de encontrar en el orden en el que esta la lista
            #for nodo en lista, lo unico que tenemos es el nombre, ocupamos usar el addNode ya que tenemos el nomrbe y eso nos regresa el nodo
            #ademas en ese metodo vamos a crear un arbol ( una lista vacia con el nombre de arvol, cada que termine un nodo lo vamos a añadir a ese árbol, es decir, vamos a crear un bosque y luego un arvol
            # al dfs visitar vamos a añadir un arbol, cada que nu arbol termine vamos a iterar uno en el bosque)
            if nodo.color == Color.BLANCO:
                tiempo = self.dfs_visit(nodo,tiempo)
           # print(f"DFS:{nodo.nombre} {nodo.d}/{nodo.f}")
            
    def dfs_visit(self, u, tiempo):
        tiempo += 1
        u.d = tiempo
        u.color = Color.GRIS
        for ady in u.adyacentes.keys():
            v = self.V[ady]
            if v.color == Color.BLANCO:
                v.p = u
                tiempo = self.dfs_visit(v,tiempo)
        u.color = Color.NEGRO
        tiempo += 1
        u.f = tiempo
        self.lista.insert(0,u) #Se marca en negro el nodo y se añade al inicio de la lista
        #print(f"DFS VISIT {u.nombre} {u.d}/{u.f}")
        return tiempo
    
    def scc(self, lista):
        #copiar y pegar el dfs y el dfs_visit añadiendo los comentarios del profe
        #para tenerlos por separado y no equivocarnos
        for nodo in self.V.values():
            nodo.color = Color.BLANCO
            nodo.p = None
        
        tiempo = 0
        bosque=[] #se crea un arreglo para el bosque donde se añadiran los arboles
        
        for nodo in lista:
            u = self.V[nodo]
            if not u.adyacentes:  #si el nodo no tiene adyacentes se omite (es un nodo aislado)
                continue 
            if u.color == Color.BLANCO:
                arbol = []
                tiempo = self.scc_visit(u,tiempo,arbol)#se crea un arreglo para los arboles
                bosque.append(arbol)#se agregan los arboles al bosque
        return bosque
    
    def scc_visit(self, u, tiempo, arbol):
        tiempo += 1
        u.d = tiempo
        u.color = Color.GRIS
        #Se añade como árbol el nodo que se visita
        arbol.append(u)
        for ady in u.adyacentes.keys():
            v = self.V[ady]
            if v.color == Color.BLANCO:
                v.p = u
                tiempo = self.scc_visit(v,tiempo, arbol)
        u.color = Color.NEGRO
        tiempo += 1
        u.f = tiempo
        return tiempo
    
    def get_lista(self):
        return self.lista
    
    def mst_kruskal(self):
        kruskal=Grafo("mst-kruskal")
        aristas=[]
        for nodo in self.V.values():
            kruskal.addNodo(nodo.nombre)
            for arco in nodo.adyacentes.values():
                aristas.append(arco)
                
        #Se aplica el "make-set"         
        for index,nodo in enumerate(kruskal.V.values()):
            nodo.id=index
        #print(kruskal)
        #Se ordenan las aristas en orden ascendentes de acuerdo a su peso/costo
        aristas.sort(key=lambda arco: arco.costo)
        
        for arista in aristas:
            #Se toman los nodos de origen y destino de cada arista
            u = kruskal.V[arista.origen]
            v = kruskal.V[arista.destino]
            #print("Origen",u,"Destino", v)
            if kruskal.find_set(u) != kruskal.find_set(v):
                kruskal.addArco(arista)
                #print(Arco(arista.destino,arista.origen,arista.costo))
                kruskal.addArco(Arco(arista.destino,arista.origen,arista.costo))
                #print(kruskal)
                kruskal.union(u, v)
        return kruskal
    
    def find_set(self, nodo):
        #print("nombre:",nodo.nombre," id: ",self.V[nodo.nombre].id)
        return self.V[nodo.nombre].id
    
    def union(self, u_origen, v_origen):
        u = self.find_set(u_origen)
        v = self.find_set(v_origen)
        self.V[v_origen.nombre].id=u
        #print("UNION")
        for nodo in self.V.values():
            #print("Nodo pre evaluación ",nodo)
            if(nodo.id==v):
                self.V[nodo.nombre].id=u
            #print("Nodo post evaluación",nodo)
                
                
    
    def mst_prim(self, nodoInicial):
        
        """
        Iniciar el nodo con el valor de 0
        Asignar el valor del siguiente nodo con el 
        Se mete la arista al nodo
        A la hora de relajar se tiene que añadir quien lo relajo
        Los nodos pueden volver a relajar a otro nodo
        """        
        prim = Grafo("mst-prim")
        for nodo in self.V.values():
            prim.addNodo(nodo.nombre)
            
        for nodo in prim.V.values():
            nodo.d = float("Inf")  #d es key
            nodo.p = None #pi es el padre

        prim.V[nodoInicial].d=0
        Q = list(prim.V.values())

        while len(Q) != 0:
            u = prim.min_q(Q)  #Se busca el que tiene el menor valor de los arcos
            Q.remove(u)
            
            for destino, arco in self.V[u.nombre].adyacentes.items(): #sacamos los adyacentes
                #print("NodoOrigen:",u.nombre,"Adyacente:", destino)
                v = prim.V[destino]
                #Si aún esta en la cola quiere decir que aún no esta de rojo
                if v in Q and arco.costo < v.d:
                    #print("Costo del arco:",arco.costo,"KeyDestino:", v.d)
                    v.p = u
                    v.d = u.d+arco.costo
                    #print("Padre de v:",v.p,"KeyDestinoActualizada:", v.d)
                    #print("")
        #Añadimos los arcos con los datos resultantes de los padres y de distancia (pi y key)
        for nodo in list(prim.V.values()):
            if nodo.p is not None:
                prim.addArco(Arco(nodo.p.nombre,nodo.nombre,nodo.d))
                prim.addArco(Arco(nodo.nombre,nodo.p.nombre,nodo.d))
                
        return prim

    def min_q(self, Q):
        minNodo = Q[0]
        for nodo in Q:
            #print("Nodo actual del for: "+nodo.nombre, "d: ",nodo.d,"Primer nodo de Q[0]",minNodo.nombre, "d: ",minNodo.d)
            if nodo.d < minNodo.d:
                minNodo = nodo
        return minNodo

    def mst_boruvka(self):
        
        #Toma el valor del arco de menor peso de cada nodo
        #Se habla como el super nodo es como si tuviera el mismo id
        #Ahora se va a las aristas que tienen menos valor en los super nodos
        #se añaden esos arcos a los super nodos
        
        #cuando todos los nodos esten en A esten en B, todos los nodos tienen que estar (son aristas las que van a faltar)
        #podría ocurrir que exista un nodo
        boruska = None
        self.getV()
        return ''

    def graficar(self):
        # Crear un grafo vacío
        #G = nx.Graph() #crear aristas
        G = nx.DiGraph()  # crear arcos

        # Añadir nodos
        for nodo in self.V.keys():
            G.add_node(nodo)

        # Añadir aristas (conexiones entre nodos)
        for arco in self.getE():
            G.add_edge(arco.origen, arco.destino, weight=arco.costo)

        # Añadir aristas de acuerdo con la estructura del árbol BFS
        # Recorremos todos los nodos almacenados en el grafo
        """
        for nodo in self.V.values():
            #Se comprueba si el nodo cuenta con un padre
            if nodo.p is not None:
                #Si cuenta con un padre se añade el 
                # nombre del nodo padre como arco de origen y 
                # el nodo actual como arco de destino
                G.add_edge(nodo.p.nombre, nodo.nombre)
       
        for nodo in self.V.values():
            #Se comprueba si el nodo cuenta con un padre
            print("Nodo: ",nodo)
            if nodo.p is not None:
                #Si cuenta con un padre se añade el 
                # nombre del nodo padre como arco de origen y 
                # el nodo actual como arco de destino
                G.add_edge(nodo.nombre,nodo.p.nombre)
        """    
        
        # Dibujar el grafo no dirigido
        #nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='black', font_size=15, font_color='red', )

        # Dibujar el grafo dirigido
        pos = nx.spring_layout(G=G, k=1)  # Posicionamiento de los nodos
        """nx.draw(G,  pos,  with_labels=True,  node_color='skyblue',  node_size=1024, edge_color='black', 
                font_size=20, font_color='red', arrows=True)"""
        nx.draw_networkx(G,pos,arrows=True,with_labels=True)
        """edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos,edge_labels=edge_labels,font_color='blue')
        nx.draw_networkx_edge_labels(G, pos,
                                     edge_labels=nx.get_edge_attributes(G, 'weight'),
                                     font_color='blue')
        """
        # Mostrar el grafo
        plt.show()
    
    def __str__(self):
        cadena = self.nombre + ": \n"
        for nodo in self.V.values():
            cadena += str(nodo)+" \n"
        return cadena
    
    """
    lso que hicismos son aristas, que pasa cuando son arcos
    
    Este sería el problema de nuestro proyecto
    proyecto final trayectoria más corta es de optimización
    
    
    bellman_ford
    Si es que hay un false quiere decir que hay ciclos negativos
    
    
    """