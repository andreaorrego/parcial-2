from Model.producto import Producto, Tipo_producto

class Animal:
    BOVINO = "Bovino"
    PORCINO = "Porcino"
    CARPINO = "Carpino"

class Antibiotico:
    def __init__(self, producto: Producto):
        if producto.tipo_producto != Tipo_producto.ANTIBIOTICO:
            raise TypeError("El producto debe ser un antibiótico")
        self.producto = producto
        self._peso: float = 0.0
        self._tipo_animal: str = "" 

    @property
    def nombre_producto(self):
        return self.producto.nombre_producto

    @property
    def registro_ICA(self):
        return self.producto.registro_ICA

    @property
    def dosis(self):
        return self.producto.dosis
    
    @property
    def concentracion(self):
        return self.producto.concentracion
    
    @property
    def frecuencia_aplicacion(self):
        return self.producto.frecuencia_aplicacion
    
    @property
    def tipo_animal(self):
        return self._tipo_animal
    
    @tipo_animal.setter
    def tipo_animal(self, valor):
        if valor not in [Animal.BOVINO, Animal.PORCINO, Animal.CARPINO]:
            raise ValueError("Tipo de animal no válido")
        self._tipo_animal = valor

    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, valor):
        if not (400 <= valor <= 600):
            raise ValueError("El peso debe de estar entre 400 y 600 kg")
        self._peso = valor

    @property
    def valor_producto(self):
        return self.producto.valor_producto
    
    def calcular_dosis(self):
        if self.tipo_animal == Animal.BOVINO:
            return (self.peso * self.producto.dosis) / self.producto.concentracion
        elif self.tipo_animal == Animal.PORCINO:
            return (self.peso * self.producto.dosis) / self.producto.concentracion
        elif self.tipo_animal == Animal.CARPINO:
            return (self.peso * self.producto.dosis) / self.producto.concentracion
        else:
            raise ValueError("Tipo de animal no válido para calcular la dosis")