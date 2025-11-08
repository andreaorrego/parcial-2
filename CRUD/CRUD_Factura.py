import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.cliente import Clientes
from Model.factura import Factura
from datetime import date

class CRUD_Factura:
    def __init__(self):
        self.facturas = []

    def crear_factura(self, cliente: Clientes):
        factura = Factura(cliente)
        self.facturas.append(factura)
        return factura
    
    def leer_facturas(self):
        return self.facturas
    
    def buscar_factura(self, fecha: date, cedula_cliente: int):
        for factura in self.facturas:
            if factura.fecha_compra == fecha and factura.cliente.cedula == cedula_cliente:
                return factura
        return None

    def actualizar_factura(self, factura: Factura, nuevo_producto):
        if factura in self.facturas:
            factura.agregar_producto(nuevo_producto)
            return True
        return False
    
    def eliminar_factura(self, factura: Factura):
        if factura in self.facturas:
            self.facturas.remove(factura)
            return True
        return False