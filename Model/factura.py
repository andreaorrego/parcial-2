import Model.cliente as clientes
from datetime import date

class factura:
    def __init__ (self, cliente: clientes):
        fecha_compra: date
        valor_factura: float = 0.0
        self.cliente = cliente