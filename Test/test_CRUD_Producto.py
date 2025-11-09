import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto
from Model.constantes import Frecuencia_aplicacion, Tipo_producto
from CRUD.CRUD_Producto import CRUD_Producto

def test_CRUD_Producto():
    CRUD = CRUD_Producto()

    producto = CRUD.crear_producto (nombre_producto = "Enrofloxacina",
                                    registro_ICA = "1842-DB",
                                    dosis = 5,
                                    concentracion = 100,
                                    frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                                    tipo_producto = Tipo_producto.ANTIBIOTICO,
                                    valor_producto = 42000)

    assert producto is not None 
    assert producto.nombre_producto == "Enrofloxacina"
    assert producto.registro_ICA == "1842-DB"
    assert producto.tipo_producto == Tipo_producto.ANTIBIOTICO
    assert len(CRUD.leer_productos()) == 1

    producto_encontrado = CRUD.buscar_producto ("1842-DB")
    assert producto_encontrado is not None
    assert producto_encontrado.nombre_producto == "Enrofloxacina"

    producto_actualizado = CRUD.actualizar_producto("1842-DB", nombre_producto = "Oxitetraciclina", valor_producto = 48000)
    assert producto_actualizado is True 
    assert producto.nombre_producto == "Oxitetraciclina"
    assert producto.valor_producto == 48000

    producto_eliminado = CRUD.eliminar_producto ("1842-DB")
    assert producto_eliminado is True
    assert len(CRUD.leer_productos()) == 0
    assert CRUD.buscar_producto("1842-DB") is None