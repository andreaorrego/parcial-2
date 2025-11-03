from datetime import date
from Model.producto import Producto, Tipo_producto, Frecuencia_aplicacion, Control_Fertilizantes, Control_Plagas

def test_producto():  
    producto1 = Producto(nombre_producto = "SEVIN XLR PLUS 480 SC",
                        registro_ICA= "2229",
                        dosis = 2.60,
                        concentracion = 480,
                        frecuencia_aplicacion = Frecuencia_aplicacion.DIAS,
                        tipo_producto = Tipo_producto.CONTROL_PLAGAS,
                        valor_producto = "28.800")
    
    producto_plaga = Control_Plagas(producto = producto1, periodo_carencia = 10)
    producto_plaga.area_aplicacion = 0.5
    dosis_calculada1 = producto_plaga.calcular_dosis(producto1)
    
    producto2 = Producto(nombre_producto = "Fosfato Monoamónico (MAP)",
                        registro_ICA= "1022-DB",
                        dosis = 100,
                        concentracion = 46, 
                        frecuencia_aplicacion = Frecuencia_aplicacion.UNICA,
                        tipo_producto = Tipo_producto.CONTROL_FERTILIZANTES,
                        valor_producto = "140.000")
    
    producto_fertilizante = Control_Fertilizantes(producto = producto2, ultima_aplicacion = date(2025,11,3))
    producto_fertilizante.area_aplicacion = 1500
    dosis_calculada2 = producto_fertilizante.calcular_dosis(producto2)

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

    assert producto_plaga.nombre_producto == "SEVIN XLR PLUS 480 SC"
    assert producto_plaga.registro_ICA == "2229"
    assert producto_plaga.dosis == 2.60
    assert producto_plaga.concentracion == 480  
    assert producto_plaga.periodo_carencia == "De 7 a 14 dias"
    assert producto_plaga.area_aplicacion == 0.5
    assert dosis_calculada1 == producto_plaga.dosis * producto_plaga.area_aplicacion
    assert producto_plaga.frecuencia_aplicacion == Frecuencia_aplicacion.DIAS
    assert producto_plaga.tipo_producto == Tipo_producto.CONTROL_PLAGAS
    assert producto_plaga.valor_producto == "28.800"

    print ("-----------------------------------")

    assert producto_fertilizante.nombre_producto == "Fosfato Monoamónico (MAP)"
    assert producto_fertilizante.registro_ICA == "1022-DB"
    assert producto_fertilizante.dosis == 100
    assert producto_fertilizante.concentracion == 46
    assert producto_fertilizante.ultima_aplicacion == date(2025,11,3)
    assert producto_fertilizante.area_aplicacion == 1500
    assert dosis_calculada2 == producto_fertilizante.dosis * producto_fertilizante.area_aplicacion
    assert producto_fertilizante.frecuencia_aplicacion == Frecuencia_aplicacion.UNICA
    assert producto_fertilizante.tipo_producto == Tipo_producto.CONTROL_FERTILIZANTES
    assert producto_fertilizante.valor_producto == "140.000"
