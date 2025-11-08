import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto
from Model.constantes import Tipo_producto, Frecuencia_aplicacion

def test_producto():  
    producto = Producto(nombre_producto = "Clorpirifos",
                        registro_ICA = "2573",
                        dosis = 2,
                        concentracion = 480,
                        frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                        tipo_producto = Tipo_producto.CONTROL_PLAGAS,
                        valor_producto = 45000)   

    print("Nombre del producto: ", producto.nombre_producto)
    print("Registro ICA: ", producto.registro_ICA)
    print("Dosis: ", producto.dosis)
    print("Concentracion: ", producto.concentracion)
    print("Frecuencia de aplicacion: ", producto.frecuencia_aplicacion)
    print("Tipo de producto: ", producto.tipo_producto)
    print("Valor del producto: ", producto.valor_producto)

    assert producto.nombre_producto == "Clorpirifos"
    assert producto.registro_ICA == "2573"
    assert producto.dosis == 2
    assert producto.concentracion == 480
    assert producto.frecuencia_aplicacion == Frecuencia_aplicacion.DIAS
    assert producto.tipo_producto == Tipo_producto.CONTROL_PLAGAS
    assert producto.valor_producto == 45000