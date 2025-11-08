import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date
from Model.producto import Producto, Tipo_producto

class Control_Fertilizantes(Producto):
    def __init__(self, producto: Producto, ultima_aplicacion: date = date.today()):
        if producto.tipo_producto != Tipo_producto.CONTROL_FERTILIZANTES:
            raise TypeError("El producto debe ser de tipo Control de Fertilizantes")
        
        super().__init__(producto.nombre_producto, 
                         producto.registro_ICA, 
                         producto.frecuencia_aplicacion, 
                         producto.dosis, 
                         producto.concentracion, 
                         producto.tipo_producto, 
                         producto.valor_producto)
        
        self.__ultima_aplicacion = ultima_aplicacion
        self.__area_aplicacion: float = 0.0

    @property
    def ultima_aplicacion(self):
        return self.__ultima_aplicacion 

    @ultima_aplicacion.setter
    def ultima_aplicacion(self, valor):
        if valor > date.today():
            raise ValueError("La fecha de última aplicación no puede ser futura")
        self.__ultima_aplicacion = valor
    
    @property
    def area_aplicacion(self):
        return self.__area_aplicacion
    
    @area_aplicacion.setter
    def area_aplicacion(self, valor):
        if valor <= 0:
            raise ValueError("El área de aplicación debe ser un valor positivo")
        self.__area_aplicacion = valor

    def calcular_dosis(self): 
        if self.__area_aplicacion <= 0:
            raise ValueError("El área tratada debe ser mayor a 0")
        return (self.dosis * self.__area_aplicacion) / self.concentracion