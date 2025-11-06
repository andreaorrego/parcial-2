from Model.cliente import Clientes
from datetime import date

class Factura:
    def __init__ (self, cliente: Clientes):
        self.fecha_compra: date = date.today()
        self.productos = []
        self.valor_factura: float = 0.0
        self.cliente = cliente
    
        cliente.agregar_factura(self)
        
    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.actualizar_precio()

    def actualizar_precio(self):
        total = 0.0
        for item in self.productos:
            if hasattr(item, 'producto'):
                total += float(item.producto.valor_producto)
            else:
                total += float(item.valor_producto)
        self.valor_factura = total


        