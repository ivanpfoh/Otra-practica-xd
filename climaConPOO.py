class dia():
    clima = ""
    temperatura = 20

    def estado(self):
        if self.clima == "soleado":
            print("El dia esta soleado,con una temperatura de:",self.temperatura, " grados.")
        elif self.clima == "nuboso":
            print("El dia esta nuboso,con una temperatura de:",self.temperatura, " grados.")
        else: 
            print("El dia esta lluvioso,con una temperatura de:",self.temperatura, " grados.")
            
    def cambiar_clima_soleado(self):
        self.clima = "soleado"
        self.temperatura = 25
    def cambiar_clima_nuboso(self):
        self.clima = "nuboso"
        self.temperatura = 15
    
    def cambiar_clima_lluvioso(self):
        self.clima = "lluvioso"
        self.temperatura = 10
        



dia1 = dia()
dia1.cambiar_clima_soleado()
dia1.estado()
dia1.cambiar_clima_nuboso()
dia1.estado()
dia1.cambiar_clima_lluvioso()
dia1.estado()