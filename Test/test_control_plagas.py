import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.producto import Producto
from Model.constantes import Tipo_producto, Frecuencia_aplicacion
from Model.control_plagas import Control_Plagas

def test_control_plagas():
    producto1 = Producto(nombre_producto = "SEVIN XLR PLUS 480 SC",
                            registro_ICA= "2229",
                            dosis = 2.60,   
                            concentracion = 480,
                            frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                            tipo_producto = Tipo_producto.CONTROL_PLAGAS,
                            valor_producto = 28800)
    
    producto_plaga = Control_Plagas(producto = producto1, periodo_carencia = 10)
    producto_plaga.area_aplicacion = 0.5
    dosis_calculada1 = producto_plaga.calcular_dosis()

    print("Nombre del producto: ", producto_plaga.nombre_producto)
    print("Registro ICA: ", producto_plaga.registro_ICA)
    print(f"Dosis:{producto_plaga.dosis} kg/hectárea")
    print(f"Concentración: {producto_plaga.concentracion} g/L")
    print(f"Periodo de carencia: {producto_plaga.periodo_carencia} dias")
    print(f"Área de aplicación: {producto_plaga.area_aplicacion} hectáreas")
    print(f"Dosis para un terreno de {producto_plaga.area_aplicacion} es de {dosis_calculada1} L")
    print("Frecuencia de la aplicación: ", producto_plaga.frecuencia_aplicacion)
    print("Tipo de producto: ", producto_plaga.tipo_producto)
    print("Precio: ", producto_plaga.valor_producto)

    assert producto_plaga.nombre_producto == "SEVIN XLR PLUS 480 SC"
    assert producto_plaga.registro_ICA == "2229"
    assert producto_plaga.dosis == 2.60
    assert producto_plaga.concentracion == 480  
    assert producto_plaga.periodo_carencia == 10
    assert producto_plaga.area_aplicacion == 0.5
    assert round(dosis_calculada1, 2) == round((producto_plaga.dosis * producto_plaga.area_aplicacion)/ producto_plaga.concentracion, 2)
    assert producto_plaga.frecuencia_aplicacion == Frecuencia_aplicacion.DIAS
    assert producto_plaga.tipo_producto == Tipo_producto.CONTROL_PLAGAS
    assert producto_plaga.valor_producto == 28800