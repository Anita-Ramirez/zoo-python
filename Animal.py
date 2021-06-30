class Animal:
    def __init__(self, nombre, edad, salud, felicidad):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
    def alimento(self):
        self.salud += 10
        self.felicidad += 10
        return self 
    
    def display_info(self):
        print(f"nombre: {self.nombre}, edad: {self.edad} salud: {self.salud}, felicidad: {self.felicidad}")
        return self