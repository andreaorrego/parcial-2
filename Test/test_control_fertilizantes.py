import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date
from Model.control_fertilizantes import Control_Fertilizantes
from Model.producto import Producto
from Model.constantes import Tipo_producto, Frecuencia_aplicacion

def test_control_fertilizantes():
    producto2 = Producto(nombre_producto = "Fosfato Monoamónico (MAP)",
                        registro_ICA= "1022-DB",
                        dosis = 100,
                        concentracion = 46, 
                        frecuencia_aplicacion = Frecuencia_aplicacion.UNICA,
                        tipo_producto = Tipo_producto.CONTROL_FERTILIZANTES,
                        valor_producto = 140000)
    
    producto_fertilizante = Control_Fertilizantes(producto = producto2, ultima_aplicacion = date(2025,11,3))
    producto_fertilizante.area_aplicacion = 1500
    dosis_calculada2 = producto_fertilizante.calcular_dosis()

    print("Nombre del producto: ", producto_fertilizante.nombre_producto)
    print("Registro ICA: ", producto_fertilizante.registro_ICA)
    print(f"Dosis: {producto_fertilizante.dosis} kg/hectárea")
    print(f"Concentración: {producto_fertilizante.concentracion} kg")
    print("Última aplicación: ", producto_fertilizante.ultima_aplicacion)
    print(f"Área de aplicación: {producto_fertilizante.area_aplicacion} hectáreas")
    print(f"Dosis para un terreno de {producto_fertilizante.area_aplicacion} es de {dosis_calculada2} kg")
    print("Frecuencia de la aplicación: ", producto_fertilizante.frecuencia_aplicacion)
    print("Tipo de producto: ", producto_fertilizante.tipo_producto)
    print("Precio: ", producto_fertilizante.valor_producto)

    assert producto_fertilizante.nombre_producto == "Fosfato Monoamónico (MAP)"
    assert producto_fertilizante.registro_ICA == "1022-DB"
    assert producto_fertilizante.dosis == 100
    assert producto_fertilizante.concentracion == 46
    assert producto_fertilizante.ultima_aplicacion == date(2025,11,3)
    assert producto_fertilizante.area_aplicacion == 1500
    assert round(dosis_calculada2, 2) == round((producto_fertilizante.dosis * producto_fertilizante.area_aplicacion)/producto_fertilizante.concentracion, 2)
    assert producto_fertilizante.frecuencia_aplicacion == Frecuencia_aplicacion.UNICA
    assert producto_fertilizante.tipo_producto == Tipo_producto.CONTROL_FERTILIZANTES
    assert producto_fertilizante.valor_producto == 140000