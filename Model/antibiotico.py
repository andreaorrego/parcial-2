import producto as Productos

class Animal:
    BOVINO = "Bovino"
    PORCINOS = "Porcinos"
    CARPINOS = "Carpinos"

class Antibiotico:
    def __init__ (self, producto: Productos):
        self.nombre_antibiotico: str = ""
        self._dosis: float = 0.0
        self._tipo_animal: str = ""  
        self._precio : float = 0.0

    @property
    def dosis(self):
        return self._dosis
    
    @dosis.setter
    def dosis(self, valor):
        if not (400 <= valor <= 600):
            raise ValueError("La dosis debe estar entre 400 y 600 mg/kg")
        self._dosis = valor

    @property
    def tipo_animal(self):
        return self._tipo_animal
    
    @tipo_animal.setter
    def tipo_animal(self, valor):
        if valor not in ["Bovino", "Porcinos", "Carpinos"]:
            raise ValueError("Tipo de animal inválido")
        self._tipo_animal = valor

    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = valor


cliente1 = Antibiotico(Productos)
cliente1.nombre_antibiotico = "Amoxicilina"
cliente1.dosis = 500
cliente1.tipo_animal = Animal.BOVINO
cliente1.precio = 15000


print ("Nombre antibiotico ", cliente1.nombre_antibiotico)
print ("dosis: ", cliente1.dosis)
print ("Tipo de animal: ", cliente1.tipo_animal)
print ("Precio: ", cliente1.precio)

