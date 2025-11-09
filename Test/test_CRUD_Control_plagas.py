import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CRUD.CRUD_Control_plagas import CRUD_Control_Plagas
from Model.producto import Producto
from Model.constantes import Frecuencia_aplicacion, Tipo_producto

@pytest.fixture
def test_CRUD_control_plagas():
    return CRUD_Control_Plagas()

@pytest.fixture
def test_producto_plagas():
    return Producto(nombre_producto = "SEVIN XLR PLUS 480 SC",
                    registro_ICA = "2229",
                    dosis = 2.60,
                    concentracion = 480,
                    frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                    tipo_producto = Tipo_producto.CONTROL_PLAGAS,
                    valor_producto = 28800)

def test_crear_plaga_valido (test_CRUD_control_plagas, test_producto_plagas):
    plaga = test_CRUD_control_plagas.crear_control_plagas(test_producto_plagas, periodo_carencia = 10)
    plaga.area_aplicacion = 0.5

    assert plaga is not None
    assert plaga.area_aplicacion == 0.5
    assert len(test_CRUD_control_plagas.leer_control_plagas()) == 1

def test_crear_plaga_invalido (test_CRUD_control_plagas):
    test_producto_invalido = Producto (nombre_producto = "Fosfato Monoamónico (MAP)",
                                       registro_ICA = "1022-DB",
                                       dosis = 100,
                                       concentracion = 46,
                                       frecuencia_aplicacion = Frecuencia_aplicacion.UNICA,
                                       tipo_producto = Tipo_producto.CONTROL_FERTILIZANTES,
                                       valor_producto = 140000)
    
    with pytest.raises(TypeError, match = "El producto debe ser de tipo Control de Plagas"):
        test_CRUD_control_plagas.crear_control_plagas(test_producto_invalido, periodo_carencia = 10)

def test_buscar_plaga (test_CRUD_control_plagas, test_producto_plagas):
    test_CRUD_control_plagas.crear_control_plagas (test_producto_plagas, periodo_carencia = 7)
    encontrado = test_CRUD_control_plagas.buscar_control_plagas("2229")
    assert encontrado is not None
    assert encontrado.nombre_producto == "SEVIN XLR PLUS 480 SC"

def test_actualizar_plaga (test_CRUD_control_plagas, test_producto_plagas):
    test_CRUD_control_plagas.crear_control_plagas (test_producto_plagas, periodo_carencia = 7)
    actualizado = test_CRUD_control_plagas .actualizar_control_plagas("2229", nuevo_periodo_carencia = 10)
    assert actualizado
    plaga1 = test_CRUD_control_plagas.buscar_control_plagas("2229")
    assert plaga1.periodo_carencia == 10

def test_eliminar_plaga (test_CRUD_control_plagas, test_producto_plagas):
    test_CRUD_control_plagas.crear_control_plagas (test_producto_plagas, periodo_carencia = 7)
    eliminado = test_CRUD_control_plagas.eliminar_control_plagas ("2229")
    assert eliminado
    assert len(test_CRUD_control_plagas.leer_control_plagas()) == 0