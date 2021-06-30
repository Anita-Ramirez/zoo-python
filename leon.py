from Animal import Animal


class Leon(Animal):
    def __init__(self, nombre, edad, salud=10,felicidad=0):
        super().__init__(nombre, edad, salud,felicidad)
        super().alimento()
        
    def alimentacion(self):
        self.salud += 11
        self.felicidad +=11
        
    def onomatopeya(self):
        print("el Leon ")
        
    def alimento(self):
        print ("el leon come")
        