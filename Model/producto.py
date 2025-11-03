from datetime import date
from dataclasses import dataclass

class Tipo_producto:
    ANTIBIOTICO = "Antibiotico"
    CONTROL_PLAGAS = "Control de Plagas"
    CONTROL_FERTILIZANTES = "Control de Fertilizantes"

class Frecuencia_aplicacion:
    UNICA = "Única vez"
    HORA = "Cada 12 horas entre 3 a 5 dias"
    HORAS = "De 12 a 24 horas entre 2 a 3 dias"
    DIA = "Cada 24 horas entre 3 a 5 dias"
    DIAS = "De 7 a 14 dias"
    SEMANA = "De 10 a 14 dias"

@dataclass
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
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion
    
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
        self._frecuencia_aplicacion = valor

@dataclass
class Control_Plagas(Producto):
    def __init__(self, producto: Producto, periodo_carencia):
        if producto.tipo_producto != Tipo_producto.CONTROL_PLAGAS:
            raise TypeError("El producto debe ser de tipo Control de Plagas")
        super().__init__(producto.nombre_producto, producto.registro_ICA, producto.frecuencia_aplicacion, 
                         producto.dosis, producto.concentracion, producto.tipo_producto, producto.valor_producto)
        self.periodo_carencia = periodo_carencia
        self.area_aplicacion: float = 0.0

    @property
    def periodo_carencia(self):
        return self._periodo_carencia
    
    @periodo_carencia.setter
    def periodo_carencia(self, valor):
        if 7 <= valor <= 14:
            self._periodo_carencia = Frecuencia_aplicacion.DIAS
        elif 10 <= valor <= 14:
            self._periodo_carencia = Frecuencia_aplicacion.SEMANA
    
    def calcular_dosis(self, producto):
        return producto.dosis * self.area_aplicacion

@dataclass
class Control_Fertilizantes(Producto):
    def __init__ (self, producto: Producto, ultima_aplicacion = date):
        if producto.tipo_producto != Tipo_producto.CONTROL_FERTILIZANTES:
            raise TypeError("El producto debe ser de tipo Control de Fertilizantes")
        super().__init__(producto.nombre_producto, producto.registro_ICA, producto.frecuencia_aplicacion, 
                         producto.dosis, producto.concentracion, producto.tipo_producto, producto.valor_producto)
        self.ultima_aplicacion = ultima_aplicacion
        self.area_aplicacion: float = 0.0

    def calcular_dosis(self, producto):
        return producto.dosis * self.area_aplicacion