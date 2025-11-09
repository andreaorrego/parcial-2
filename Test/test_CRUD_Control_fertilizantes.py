import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date, timedelta
from CRUD.CRUD_Control_fertilizantes import CRUD_Control_Fertilizantes
from Model.producto import Producto
from Model.constantes import Frecuencia_aplicacion, Tipo_producto


@pytest.fixture
def test_CRUD_control_fertilizante():
    return CRUD_Control_Fertilizantes()

@pytest.fixture
def test_producto_fertilizante():
    return Producto(nombre_producto = "Fosfato Monoamónico (MAP)",
                    registro_ICA = "1022-DB",
                    dosis = 100,
                    concentracion = 46,
                    frecuencia_aplicacion = Frecuencia_aplicacion.UNICA,
                    tipo_producto = Tipo_producto.CONTROL_FERTILIZANTES,
                    valor_producto = 140000)

def test_crear_fertilizante_valido (test_CRUD_control_fertilizante, test_producto_fertilizante):
    fertilizante = test_CRUD_control_fertilizante.crear_control_fertilizantes(test_producto_fertilizante, ultima_aplicacion = date.today())
    fertilizante.area_aplicacion = 1500

    assert fertilizante is not None
    assert fertilizante.area_aplicacion == 1500
    assert len(test_CRUD_control_fertilizante.leer_control_fertilizantes()) == 1

def test_crear_fertilizante_invalido (test_CRUD_control_fertilizante):
    test_producto_invalido = Producto (nombre_producto = "Enrofloxacina",
                                       registro_ICA = "1842-DB",
                                       dosis = 5,
                                       concentracion = 100,
                                       frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                                       tipo_producto = Tipo_producto.ANTIBIOTICO,
                                       valor_producto = 42000)
    
    with pytest.raises(TypeError, match = "El producto debe ser de tipo Control de Fertilizantes"):
        test_CRUD_control_fertilizante.crear_control_fertilizantes(test_producto_invalido, ultima_aplicacion = date.today())

def test_buscar_fertilizante (test_CRUD_control_fertilizante, test_producto_fertilizante):
    test_CRUD_control_fertilizante.crear_control_fertilizantes (test_producto_fertilizante, ultima_aplicacion = date.today())
    encontrado = test_CRUD_control_fertilizante.buscar_control_fertilizantes("1022-DB")
    assert encontrado is not None 
    assert encontrado.nombre_producto == "Fosfato Monoamónico (MAP)"

def test_actualizar_fertilizante (test_CRUD_control_fertilizante, test_producto_fertilizante):
    test_CRUD_control_fertilizante.crear_control_fertilizantes (test_producto_fertilizante, ultima_aplicacion = date.today())

    nueva_fecha = date.today() - timedelta(days = 3)
    
    actualizado = test_CRUD_control_fertilizante.actualizar_control_fertilizantes ("1022-DB", nueva_ultima_aplicacion = nueva_fecha, nueva_area_aplicacion = 2000)
    
    assert actualizado
    fertilizante1 = test_CRUD_control_fertilizante.buscar_control_fertilizantes ("1022-DB")
    assert fertilizante1.area_aplicacion == 2000
    assert fertilizante1.ultima_aplicacion == nueva_fecha

def test_eliminar_plaga (test_CRUD_control_fertilizante, test_producto_fertilizante):
    test_CRUD_control_fertilizante.crear_control_fertilizantes (test_producto_fertilizante, ultima_aplicacion = date.today())
    eliminado = test_CRUD_control_fertilizante.eliminar_control_fertilizantes("1022-DB")

    assert eliminado
    assert len(test_CRUD_control_fertilizante.leer_control_fertilizantes()) == 0