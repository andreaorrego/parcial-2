from Model.cliente import Clientes
from Model.factura import Factura
from Model.producto import Producto, Control_Fertilizantes, Control_Plagas, Frecuencia_aplicacion, Tipo_producto
from Model.antibiotico import Antibiotico
from datetime import date

def test_factura():
    cliente1 = Clientes(nombre_cliente = "Andrea Orrego", cedula = 1192771677, celular = 3044683982)
    factura1 = Factura(cliente = cliente1)
    
    producto1 = Producto(nombre_producto = "Oxitetraciclina", registro_ICA = "1177-DB", dosis = 10, concentracion = 200,
                        frecuencia_aplicacion = Frecuencia_aplicacion.HORA, tipo_producto = Tipo_producto.ANTIBIOTICO, valor_producto = 22800)
    antibiotico1 = Antibiotico(producto1)
    
    producto2 = Producto(nombre_producto = "SEVIN XLR PLUS 480 SC", registro_ICA = "2229", dosis = 2.60, concentracion = 480,
                        frecuencia_aplicacion = Frecuencia_aplicacion.DIAS, tipo_producto = Tipo_producto.CONTROL_PLAGAS, valor_producto = 28000)
    fertilizante1 = Control_Plagas(producto2, periodo_carencia = 10)
    fertilizante1.area_aplicacion = 0.5

    producto3 = Producto(nombre_producto = "Fosfato Monoamónico (MAP)", registro_ICA = "1022-DB", dosis = 100, concentracion = 46,
                        frecuencia_aplicacion = Frecuencia_aplicacion.UNICA, tipo_producto = Tipo_producto.CONTROL_FERTILIZANTES, valor_producto = 140000)
    plaga1 = Control_Fertilizantes(producto3, ultima_aplicacion = date(2025,11,3))
    plaga1.area_aplicacion = 1500

    factura1.fecha_compra = date(2025,11,3)

    factura1.agregar_producto(antibiotico1)
    factura1.agregar_producto(fertilizante1)
    factura1.agregar_producto(plaga1)

    print("Factura de: ", factura1.cliente.nombre_cliente)
    print("Cédula: ", factura1.cliente.cedula)
    print("Celular: ", factura1.cliente.celular)
    print("Fecha de compra: ", factura1.fecha_compra)
    print("Valor de la factura: ", factura1.valor_factura)

    assert factura1.cliente.nombre_cliente == "Andrea Orrego"
    assert factura1.cliente.cedula == 1192771677
    assert factura1.cliente.celular == 3044683982
    assert factura1.fecha_compra == date(2025,11,3)
    assert factura1.valor_factura == 22800 + 28000 + 140000