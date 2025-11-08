import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date
from Model.producto import Producto
from Model.control_fertilizantes import Control_Fertilizantes

class CRUD_Control_Fertilizantes:
    def __init__(self):
        self.__control_fertilizantes = []

    def crear_control_fertilizantes(self, producto: Producto, ultima_aplicacion: date = date.today()): 
        control_fertilizantes = Control_Fertilizantes(producto, ultima_aplicacion)
        self.__control_fertilizantes.append(control_fertilizantes)
        return control_fertilizantes

    def leer_control_fertilizantes(self):
        return self.__control_fertilizantes

    def buscar_control_fertilizantes(self, registro_ICA):
        for control_fertilizante in self.__control_fertilizantes:
            if control_fertilizante.registro_ICA == registro_ICA:
                return control_fertilizante
        return None

    def actualizar_control_fertilizantes(self, registro_ICA, nueva_ultima_aplicacion=None, nueva_area_aplicacion=None):
        control_fertilizante = self.buscar_control_fertilizantes(registro_ICA)
        if control_fertilizante:
            if nueva_ultima_aplicacion:
                control_fertilizante.ultima_aplicacion = nueva_ultima_aplicacion
            if nueva_area_aplicacion:
                control_fertilizante.area_aplicacion = nueva_area_aplicacion
            return True
        return False

    def eliminar_control_fertilizantes(self, registro_ICA):
        control_fertilizante = self.buscar_control_fertilizantes(registro_ICA)
        if control_fertilizante:
            self.__control_fertilizantes.remove(control_fertilizante)
            return True
        return False