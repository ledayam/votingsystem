from abc import ABCMeta

class ModeloAbstracto():
    def __init__(self,datos):
        for llave,valor in datos.items():
            setattr(self,llave,valor)
        