from datetime import date
from dataclasses import dataclass

@dataclass
class producto:
    def __init__(self):
        registro_ICA: str = ""
        nombre_producto: str = ""
        frecuencia_aplicacion: str = ""
        valor_producto: int = ""

@dataclass
class control_plagas(producto):
    def __init__ (self):
        periodo_carencia: int = 0

@dataclass
class control_fertilizantes(producto):
    def __init__ (self):
        ultima_aplicacion: date
