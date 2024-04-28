

class computadora():
    def __init__(self, marca, ram, procesador, almacenamiento):
        self.marca = marca
        self.ram = ram
        self.procesador = procesador
        self.almacenamiento = almacenamiento
        self.estado = False
        self.conectada = False
    
    def estado1(self):
        if self.estado == False:
            return("la computadora se encuentra apagada.")
        else:
            return("la computadora se encuentra prendida")
    
    def encender(self, newestado):
        self.estado = newestado
    
    def apagar(self, newestado):
        self.estado = newestado
    
    def estadoo(self):
        print("La marca de la computadora es: ",self.marca,", contiene ",self.ram,"de ram, contiene",self.almacenamiento,"de almacentamiento, un procesador ",self.procesador," y ", self.estado1())

class computadoraGamer(computadora):
    modoGamer = False
    def activacionGamer(self):
        self.modoGamer = True
        
    def estadoModoGamer(self):
        if self.modoGamer:
            print("el Modo gamer estado activado") 
        else:
            print("el Modo gamer esta desactivado")

    def estadoo(self):
        print("La marca de la computadora es: ",self.marca,", contiene ",self.ram,"de ram, contiene",self.almacenamiento,"de almacentamiento, un procesador ",self.procesador," , ", self.estado1(), " y ", self.estadoModoGamer())

miComputadora = computadora("asus", 16, "i5", 480)
miComputadora.estadoo()
computadoraGaming = computadoraGamer("Razer", 32, "i9", 2000)
computadoraGaming.estadoModoGamer()

class internet():
    def __init__(self, dispositivos):
        self.dispositivos = dispositivos
    
    def conectarDispositivo(self, dispositivos):
        self.dispositivos += dispositivos
    
    def estadoInternet(self):
        print(int(self.dispositivos))
        

miInternet = internet(3)
miInternet.conectarDispositivo(1)
miInternet.dispositivos()
