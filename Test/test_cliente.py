import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.cliente import Clientes
from Model.factura import Factura

def test_cliente():
    cliente1 = Clientes(nombre_cliente = "Andrea Orrego", cedula = 1192771677)

    print("Nombre del cliente: ", cliente1.nombre_cliente)
    print("Cédula del cliente: ", cliente1.cedula)

    assert cliente1.nombre_cliente == "Andrea Orrego"
    assert cliente1.cedula == 1192771677
    
    cliente1.nombre_cliente = "Nuevo nombre"
    assert cliente1.nombre_cliente == "Nuevo nombre"

    try: 
        cliente1.nombre_cliente ="  "
        assert False, "Value Error"
    except ValueError:
        pass

    factura = Factura(cliente1)
    assert len(cliente1.facturas) == 1
    assert cliente1.facturas[0] == factura


