import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto, Tipo_producto
from Model.constantes import Tipo_producto
from Model.antibiotico import Antibiotico

class CRUD_Antibiotico:
    def __init__(self):
        self.antibioticos = []

    def crear_antibiotico(self, producto: Producto):
        if producto.tipo_producto != Tipo_producto.ANTIBIOTICO:
            print("El producto no es un antibiótico.")
            return None
        antibiotico = Antibiotico(producto)
        self.antibioticos.append(antibiotico)
        return antibiotico


    def leer_antibioticos(self):
        return self.antibioticos
    
    def buscar_antibiotico(self, nombre_producto: str):
        for antibiotico in self.antibioticos:
            if antibiotico.nombre_producto == nombre_producto:
                return antibiotico
        return None

    def actualizar_antibiotico(self, nombre_producto: str, nuevo_peso: float = None, nuevo_tipo_animal: str = None):
        antibiotico = self.buscar_antibiotico(nombre_producto)
        if antibiotico:
            if nuevo_peso is not None:
                antibiotico.peso = nuevo_peso
            if nuevo_tipo_animal is not None:
                antibiotico.tipo_animal = nuevo_tipo_animal
            return True
        return False
    
    def eliminar_antibiotico(self, nombre_producto: str):
        antibiotico = self.buscar_antibiotico(nombre_producto)
        if antibiotico:
            self.antibioticos.remove(antibiotico)
            return True
        return False
