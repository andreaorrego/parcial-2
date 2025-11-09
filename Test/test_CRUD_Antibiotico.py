import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto
from Model.antibiotico import Antibiotico
from Model.constantes import Tipo_producto, Frecuencia_aplicacion, Animal
from CRUD.CRUD_Antibiotico import CRUD_Antibiotico

@pytest.fixture
def test_CRUD_antibiotico():
    return CRUD_Antibiotico()

@pytest.fixture
def test_producto_antibiotico():
    return Producto(nombre_producto = "Oxitetraciclina", 
                    registro_ICA = "1177- DB", 
                    dosis = 10, 
                    concentracion = 200, 
                    frecuencia_aplicacion = Frecuencia_aplicacion.HORA, 
                    tipo_producto = Tipo_producto.ANTIBIOTICO, 
                    valor_producto = 22800)

def test_crear_antibiotico_valido (test_CRUD_antibiotico, test_producto_antibiotico):
    antibiotico = test_CRUD_antibiotico.crear_antibiotico(test_producto_antibiotico)
    antibiotico.peso = 400
    antibiotico.tipo_animal = Animal.BOVINO

    assert antibiotico is not None
    assert antibiotico.peso == 400
    assert antibiotico.tipo_animal == Animal.BOVINO
    assert len(test_CRUD_antibiotico.leer_antibioticos()) == 1

def test_crear_antibiotico_invalido (test_CRUD_antibiotico):
    test_producto_invalido = Producto (nombre_producto = "Fosfato Monoamónico (MAP)",
                                       registro_ICA = "1022-DB",
                                       dosis = 100,
                                       concentracion = 46,
                                       frecuencia_aplicacion = Frecuencia_aplicacion.UNICA,
                                       tipo_producto = Tipo_producto.CONTROL_FERTILIZANTES,
                                       valor_producto = 140000)
    
    antibiotico2 = test_CRUD_antibiotico.crear_antibiotico(test_producto_invalido)
    assert antibiotico2 is None
    assert len(test_CRUD_antibiotico.leer_antibioticos()) == 0

def test_buscar_antibiotico(test_CRUD_antibiotico, test_producto_antibiotico):
    test_CRUD_antibiotico.crear_antibiotico (test_producto_antibiotico)
    encontrado = test_CRUD_antibiotico.buscar_antibiotico("Oxitetraciclina")
    assert encontrado is not None
    assert encontrado.nombre_producto == "Oxitetraciclina"
    
def test_actualizar_antibiotico(test_CRUD_antibiotico, test_producto_antibiotico):
    test_CRUD_antibiotico.crear_antibiotico(test_producto_antibiotico)
    actualizado = test_CRUD_antibiotico.actualizar_antibiotico("Oxitetraciclina",
                                                                nuevo_peso = 430, 
                                                                nuevo_tipo_animal = Animal.BOVINO)
    assert actualizado
    antibiotico = test_CRUD_antibiotico.buscar_antibiotico("Oxitetraciclina")
    assert antibiotico.peso == 430
    assert antibiotico.tipo_animal == Animal.BOVINO

def test_eliminar_antibiotico(test_CRUD_antibiotico, test_producto_antibiotico):
    test_CRUD_antibiotico.crear_antibiotico(test_producto_antibiotico)
    eliminado = test_CRUD_antibiotico.eliminar_antibiotico("Oxitetraciclina")
    assert eliminado
    assert len(test_CRUD_antibiotico.leer_antibioticos()) == 0
