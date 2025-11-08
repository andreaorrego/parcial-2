import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.cliente import Clientes

class CRUD_Cliente:
    def __init__(self):
        self.__clientes = []

    def crear_cliente(self, nombre, cedula):
        cliente = Clientes(nombre, cedula)
        self.__clientes.append(cliente)
        return cliente

    def leer_clientes(self):
        return self.__clientes

    def buscar_cliente(self, cedula):
        for cliente in self.__clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def actualizar_cliente(self, cedula, nuevo_nombre=None):
        cliente = self.buscar_cliente(cedula)
        if cliente and nuevo_nombre:
            cliente.nombre_cliente = nuevo_nombre
            return True
        return False

    def eliminar_cliente(self, cedula):
        cliente = self.buscar_cliente(cedula)
        if cliente:
            self.__clientes.remove(cliente)
            return True
        return False
