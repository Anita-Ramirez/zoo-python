from Animal import Animal

class Tigre(Animal):
    
    def __init__(self, nombre, edad, salud=10,felicidad=10):
        super().__init__(nombre, edad, salud,felicidad)
        super().alimento()
        
    def alimentacion(self):
        self.salud += 12
        self.felicidad +=12
        
    def habitats(self):
        print ("el tigre vive en:")
    
    def colectivo(self):
        if self.vivenengrupos == "SI":
            print (f"error, los tigres no viven de forma colectiva")
        else:
            print(f"el tigre es un animal solitario")
            
