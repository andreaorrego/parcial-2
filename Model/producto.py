from dataclasses import dataclass
from Model.constantes import Tipo_producto, Frecuencia_aplicacion

class Producto:
    def __init__(self, nombre_producto, registro_ICA, frecuencia_aplicacion, dosis, 
                 concentracion, tipo_producto, valor_producto):
        self.nombre_producto = nombre_producto
        self.registro_ICA = registro_ICA
        self.frecuencia_aplicacion = frecuencia_aplicacion
        self.dosis = dosis
        self.concentracion = concentracion
        self.tipo_producto = tipo_producto
        self.valor_producto = valor_producto
    
    @property
    def nombre_producto(self):
        return self.__nombre_producto   
    
    @nombre_producto.setter
    def nombre_producto(self, valor):   
        self.__nombre_producto = valor
    
    @property
    def registro_ICA(self):
        return self.__registro_ICA
    
    @registro_ICA.setter
    def registro_ICA(self, valor):
        self.__registro_ICA = valor

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion
    
    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, valor):
        if valor not in [
            Frecuencia_aplicacion.UNICA,
            Frecuencia_aplicacion.HORA,
            Frecuencia_aplicacion.HORAS,
            Frecuencia_aplicacion.DIA,
            Frecuencia_aplicacion.DIAS,
            Frecuencia_aplicacion.SEMANA
        ]:
            raise ValueError("Frecuencia de aplicación no válida")
        self.__frecuencia_aplicacion = valor

    @property
    def dosis(self):
        return self.__dosis
    
    @dosis.setter
    def dosis(self, valor):
        if valor <= 0:
            raise ValueError("La dosis debe ser un valor positivo")
        self.__dosis = valor
    
    @property
    def concentracion(self):
        return self.__concentracion
    
    @concentracion.setter
    def concentracion(self, valor):
        if valor <= 0:
            raise ValueError("La concentración debe ser un valor positivo")
        self.__concentracion = valor

    @property
    def tipo_producto(self):
        return self.__tipo_producto
    
    @tipo_producto.setter
    def tipo_producto(self, valor):
        if valor not in [
            Tipo_producto.ANTIBIOTICO,
            Tipo_producto.CONTROL_PLAGAS,
            Tipo_producto.CONTROL_FERTILIZANTES
        ]:
            raise ValueError("Tipo de producto no válido")
        self.__tipo_producto = valor
    
    @property
    def valor_producto(self):
        return self.__valor_producto
    
    @valor_producto.setter
    def valor_producto(self, valor):
        if valor < 0:
            raise ValueError("El valor del producto no puede ser negativo")
        self.__valor_producto = valor

    