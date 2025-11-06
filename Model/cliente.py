from factura import Factura 

class Clientes:
    def __init__(self, nombre_cliente, cedula):
        self.__nombre_cliente = nombre_cliente
        self.__cedula = cedula
        self.__facturas = []

    @property
    def nombre_cliente(self):
        return self.__nombre_cliente
    
    @nombre_cliente.setter
    def nombre_cliente(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre_cliente = valor

    @property
    def cedula(self):
        return self.__cedula
    
    @property
    def facturas(self):
        return self.__facturas

    def agregar_factura(self, factura):
        self.__facturas.append(factura)