from enum import Enum

class Color(Enum):
    GRIS = 1
    BLANCO = 2
    NEGRO = 3


class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.d = float("Inf")
        self.f = 0
        self.p = None #NOMBRE DEL PADRE
        self.adyacentes = {}
        self.color = Color.BLANCO
        self.id = 0
        
    def addAdyacentes(self,arco):
        if self.nombre == arco.origen:
            self.adyacentes[arco.destino]=arco
    
    def __str__(self):
        cadena = str(self.nombre)+" id:"+str(self.id)+ " f:"+str(self.d)+"/"+str(self.f)+" p: -> "
        for destino,arco in self.adyacentes.items():
            cadena += str(destino) + ":" + str(arco.costo) + ", "
        return cadena
    