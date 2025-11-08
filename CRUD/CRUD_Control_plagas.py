import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto, Tipo_producto
from Model.control_plagas import Control_Plagas

class CRUD_Control_Plagas:
    def __init__(self):
        self.__control_plagas = []

    def crear_control_plagas(self, producto: Producto, periodo_carencia):
        if producto.tipo_producto != Tipo_producto.CONTROL_PLAGAS:
            raise TypeError("El producto debe ser de tipo Control de Plagas")
        control_plagas = Control_Plagas(producto, periodo_carencia)
        self.__control_plagas.append(control_plagas)
        return control_plagas

    def leer_control_plagas(self):
        return self.__control_plagas

    def buscar_control_plagas(self, registro_ICA):
        for control in self.__control_plagas:
            if control.registro_ICA == registro_ICA:
                return control
        return None

    def actualizar_control_plagas(self, registro_ICA, nuevo_periodo_carencia=None):
        control = self.buscar_control_plagas(registro_ICA)
        if control and nuevo_periodo_carencia:
            control.periodo_carencia = nuevo_periodo_carencia
            return True
        return False

    def eliminar_control_plagas(self, registro_ICA):
        control = self.buscar_control_plagas(registro_ICA)
        if control:
            self.__control_plagas.remove(control)
            return True
        return False