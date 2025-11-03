from Model.cliente import Clientes
from Model.factura import Factura
from datetime import date

def test_factura():
    factura1 = Factura(Clientes(nombre_cliente = "Andrea Orrego", cedula = 1192771677, celular = 3044683982))

    factura1.fecha_compra = date(2025,11,3)
    factura1.valor_factura = 250000

    print("Factura de: ", factura1.cliente.nombre_cliente)
    print("Cédula: ", factura1.cliente.cedula)
    print("Celular: ", factura1.cliente.celular)
    print("Fecha de compra: ", factura1.fecha_compra)
    print("Valor de la factura: ", factura1.valor_factura)

    assert factura1.cliente.nombre_cliente == "Andrea Orrego"
    assert factura1.cliente.cedula == 1192771677
    assert factura1.cliente.celular == 3044683982
    assert factura1.fecha_compra == date(2025,11,3)
    assert factura1.valor_factura == 250000