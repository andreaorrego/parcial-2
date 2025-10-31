from datetime import date
from dataclasses import dataclass

@dataclass
class Producto:
    def __init__(self):
        self.registro_ICA: str = ""
        self.nombre_producto: str = ""
        self.frecuencia_aplicacion: str = ""
        self.valor_producto: int = 0

@dataclass
class Control_Plagas(Producto):
    def __init__ (self):
        self.periodo_carencia: int = 0

@dataclass
class Control_Fertilizantes(Producto):
    def __init__ (self):
        self.ultima_aplicacion: date

cliente1 = Producto
cliente1.nombre_producto = "ibuprofeno"
cliente1.frecuencia_aplicacion = "15 dias"
cliente1.valor_producto = 5300

print("Nombre del producto: ", cliente1.nombre_producto)
print("frecuencia de aplicacion", cliente1.frecuencia_aplicacion)
print("precio", cliente1.valor_producto)
