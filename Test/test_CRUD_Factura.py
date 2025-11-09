import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date
from CRUD.CRUD_Factura import CRUD_Factura
from Model.producto import Producto
from Model.constantes import Tipo_producto, Frecuencia_aplicacion


def test_CRUD_Factura():
    from Model.cliente import Clientes
    CRUD = CRUD_Factura()

    cliente = Clientes(nombre_cliente = "Andrea Orrego", cedula = 1192771677)
    factura = CRUD.crear_factura(cliente)

    assert factura is not None 
    assert factura.cliente.nombre_cliente == "Andrea Orrego"
    assert len(CRUD.leer_facturas()) == 1

    factura_encontrada = CRUD.buscar_factura(factura.fecha_compra, cliente.cedula)
    assert factura_encontrada == factura

    producto = Producto(nombre_producto = "Enrofloxacina",
                        registro_ICA = "1842-DB",
                        dosis = 5,
                        concentracion = 100,
                        frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                        tipo_producto = Tipo_producto.ANTIBIOTICO,
                        valor_producto = 42000)
    
    factura_actualizada = CRUD.actualizar_factura (factura, producto)
    assert factura_actualizada is True
    assert len(factura.productos) > 0

    factura_eliminada = CRUD.eliminar_factura(factura)
    assert factura_eliminada is True 
    assert len(CRUD.leer_facturas()) == 0