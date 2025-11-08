import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CRUD.CRUD_Cliente import CRUD_cliente

def test_CRUD_clientes():
    from Model.cliente import Clientes
    CRUD = CRUD_cliente()

    cliente1 = CRUD.crear_cliente ("Andrea Orrego", 1192771677)
    assert cliente1.nombre_cliente == "Andrea Orrego"
    assert cliente1.cedula == 1192771677
    assert len (CRUD.clientes) == 1

    cliente_encontrado = CRUD.buscar_cliente(1192771677)
    assert cliente_encontrado == cliente1

    cliente_actualizado = CRUD.actualizar_cliente(1192771677, "Nuevo nombre")
    assert cliente_actualizado is True
    assert cliente1.nombre_cliente == "Nuevo nombre"

    cliente_eliminado = CRUD.eliminar_cliente ()