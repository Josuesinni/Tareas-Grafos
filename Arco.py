class Arco:
    def __init__(self, origen, destino, costo):
        self.origen = origen
        self.destino = destino
        self.costo = costo
    def __str__(self):
        return self.origen +"->"+self.destino+":"+str(self.costo)