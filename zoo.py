from Animal import Animal
from  leon import Leon
from  tigre import Tigre
from  oso import Oso

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add(self, animal):
        self.animals.append(animal)
    
    def mostraranimals(self):
        for Animal in self.animals:
            Animal.display_info()
    
    def alimentartodos(self):
        for animal in zoo1.animals:
            animal.alimentacion()
        return self
    
    def alimentartodos(self):
        for animal in zoo1.animals:
            animal.alimentacion()
        return self
    
    
                
zoo1 = Zoo("John's Zoo")
tigre1= Tigre("ana",30) 
#stigre1.colectivo("si")

leon1=Leon("jose",5)
oso1=Oso("osito",5)

zoo1.add(leon1)
zoo1.add(oso1)
zoo1.add(tigre1)
zoo1.mostraranimals()
zoo1.alimentartodos()
zoo1.mostraranimals()
zoor


