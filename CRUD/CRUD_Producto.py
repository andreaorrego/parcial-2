import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dataclasses import dataclass
from Model.producto import Producto

class CRUD_Producto:
    def __init__(self):
        self.__productos = []

    def crear_producto(self, nombre_producto, registro_ICA, frecuencia_aplicacion, dosis, 
                       concentracion, tipo_producto, valor_producto):
        producto = Producto(nombre_producto, registro_ICA, frecuencia_aplicacion, dosis, 
                           concentracion, tipo_producto, valor_producto)
        self.__productos.append(producto)
        return producto

    def leer_productos(self):
        return self.__productos

    def buscar_producto(self, registro_ICA):
        for producto in self.__productos:
            if producto.registro_ICA == registro_ICA:
                return producto
        return None

    def actualizar_producto(self, registro_ICA, **kwargs):
        producto = self.buscar_producto(registro_ICA)
        if producto:
            for key, value in kwargs.items():
                if hasattr(producto, key):
                    setattr(producto, key, value)
            return True
        return False

    def eliminar_producto(self, registro_ICA):
        producto = self.buscar_producto(registro_ICA)
        if producto:
            self.__productos.remove(producto)
            return True
        return False