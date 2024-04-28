#Prueba de clases


class elfo_de_sangre:
    def __init__(self, vida, mana, defensa, ataque):
        self.vida = vida
        self.mana = mana
        self.defensa = defensa
        self.ataque = ataque
    
    def atributos(self):
        print(self.vida)
        print(self.mana)
        print(self.defensa)
        print(self.ataque)
        
class paladin(elfo_de_sangre):
    def __init__(self, vida, mana, defensa, ataque):
        super().__init__(vida, mana, defensa, ataque)

class brujo(elfo_de_sangre):
    def __init__(self, vida, mana, defensa,ataque):
        super().__init__(vida, mana, defensa, ataque)
        self.drenar_alma = 10
        self.drenar_vida = 10
        self.drenar_mana = 20
        
        
personaje1 = elfo_de_sangre(80,80,80,80)
def personaje(personaje1):
    personaje1.atributos()

personaje(personaje1)
starmack = paladin("Starmack", 100, 100, 10)

starmack.atributos()

