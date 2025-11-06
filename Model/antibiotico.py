from Model.producto import Producto, Tipo_producto
from Model.constantes import Tipo_producto, Animal

class Antibiotico:
    def __init__(self, producto: Producto):
        if producto.tipo_producto != Tipo_producto.ANTIBIOTICO:
            raise TypeError("El producto debe ser un antibiótico")
        super().__init__(producto.nombre_producto, producto.registro_ICA, producto.frecuencia_aplicacion, 
                         producto.dosis, producto.concentracion, producto.tipo_producto, producto.valor_producto)
        self.__peso: float = 0.0
        self.__tipo_animal: str = "" 
    
    @property
    def tipo_animal(self):
        return self.__tipo_animal
    
    @tipo_animal.setter
    def tipo_animal(self, valor):
        if valor not in [Animal.BOVINO, Animal.PORCINO, Animal.CARPINO]:
            raise ValueError("Tipo de animal no válido")
        self.__tipo_animal = valor

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, valor):
        if not (400 <= valor <= 600):
            raise ValueError("El peso debe de estar entre 400 y 600 kg")
        self.__peso = valor
    
    def calcular_dosis(self):
        if not self.__tipo_animal:
            raise ValueError("Debe especificar el tipo de animal antes de calcular la dosis.")
        return (self.__peso * self.dosis) / self.concentracion