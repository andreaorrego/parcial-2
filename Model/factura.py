from cliente import cliente1
from datetime import date

class Factura:
    def __init__ (self, cliente):
        self.fecha_compra: date = date.today()
        self.valor_factura: float = 0.0
        self.cliente = cliente


factura1 = Factura(cliente1)
factura1.valor_factura = 250000

print ("Factura de: ", factura1.cliente.nombre_cliente)
print ("cedula: ", factura1.cliente.cedula)
print ("Fecha de compra: ", factura1.fecha_compra)
print ("Valor de la factura: ", factura1.valor_factura)

