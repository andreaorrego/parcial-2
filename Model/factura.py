from Model.cliente import Clientes
from datetime import date

class Factura:
    def __init__ (self, cliente: Clientes):
        self.fecha_compra: date = date.today()
        self.valor_factura: float = 0.0
        self.cliente = cliente
