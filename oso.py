from Animal import Animal

class Oso(Animal):
    def __init__(self, nombre, edad, salud=10,felicidad=10):
        super().__init__(nombre, edad, salud,felicidad)
        super().alimento()
    
    def alimentacion(self):
        self.salud += 13
        self.felicidad +=13
    
