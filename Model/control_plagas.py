import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto
from Model.constantes import Tipo_producto, Frecuencia_aplicacion

class Control_Plagas(Producto):
    def __init__(self, producto: Producto, periodo_carencia):
        if producto.tipo_producto != Tipo_producto.CONTROL_PLAGAS:
            raise TypeError("El producto debe ser de tipo Control de Plagas")
        
        super().__init__(nombre_producto = producto.nombre_producto, 
                         registro_ICA = producto.registro_ICA, 
                         frecuencia_aplicacion = producto.frecuencia_aplicacion, 
                         dosis = producto.dosis, 
                         concentracion = producto.concentracion, 
                         tipo_producto = producto.tipo_producto, 
                         valor_producto = producto.valor_producto)
        
        self.__periodo_carencia = periodo_carencia
        self.__area_aplicacion: float = 0.0

    @property
    def periodo_carencia(self):
        return self.__periodo_carencia
    
    @periodo_carencia.setter
    def periodo_carencia(self, valor):
        if 7 <= valor <= 14:
            self.__periodo_carencia = valor
        elif 10 <= valor <= 14:
            self.__periodo_carencia = valor
        else:
            raise ValueError("El periodo de carencia no está en un rango válido")
    
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