

class lampara():
    def __init__(self):
        self.__estado = True

    def estado(self):
        if(self.__estado):
            print("La lampara esta encendida.")
        else:
            print("La lampara esta apagada.")
    
    def cambiar_estado(self, nuevo_estado):
        self.__estado = nuevo_estado


mi_lampara = lampara()
mi_lampara.estado()
mi_lampara.cambiar_estado(False)
mi_lampara.estado()
