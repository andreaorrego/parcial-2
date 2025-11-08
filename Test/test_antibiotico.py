import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Model.antibiotico import Antibiotico
from Model.constantes import Animal, Tipo_producto, Frecuencia_aplicacion
from Model.producto import Producto

def test_antibiotico():
    producto1 = Producto(nombre_producto = "Oxitetraciclina",
                        registro_ICA= "1177-DB",
                        dosis = 10, 
                        concentracion = 200,
                        frecuencia_aplicacion = Frecuencia_aplicacion.HORA,
                        tipo_producto = Tipo_producto.ANTIBIOTICO,
                        valor_producto= 22800)
    
    antibiotico1 = Antibiotico(producto = producto1)
    antibiotico1.tipo_animal = Animal.BOVINO
    antibiotico1.peso = 427
    dosis_calculada1 = antibiotico1.calcular_dosis()

    producto2 = Producto(nombre_producto = "Dihidroestreptomicina",
                        registro_ICA= "1910-DB",
                        dosis = 10, 
                        concentracion = 250,
                        frecuencia_aplicacion = Frecuencia_aplicacion.HORAS,
                        tipo_producto = Tipo_producto.ANTIBIOTICO,
                        valor_producto= 39600)
    
    antibiotico2 = Antibiotico(producto = producto2)
    antibiotico2.tipo_animal = Animal.PORCINO
    antibiotico2.peso = 549
    dosis_calculada2 = antibiotico2.calcular_dosis()

    producto3 = Producto(nombre_producto = "Tilosina",
                        registro_ICA= "7731-MV",
                        dosis = 10, 
                        concentracion = 200,
                        frecuencia_aplicacion = Frecuencia_aplicacion.DIA,
                        tipo_producto = Tipo_producto.ANTIBIOTICO,
                        valor_producto= 34900)
    
    antibiotico3 = Antibiotico(producto = producto3)
    antibiotico3.tipo_animal = Animal.CARPINO
    antibiotico3.peso = 483
    dosis_calculada3 = antibiotico3.calcular_dosis()

    print("Nombre del producto: ", antibiotico1.nombre_producto)
    print("Registro ICA: ", antibiotico1.registro_ICA)
    print(f"Dosis: {antibiotico1.dosis} mg/kg")
    print(f"Dosis para un {antibiotico1.tipo_animal} de {antibiotico1.peso} kg es de {dosis_calculada1} mg/kg")
    print("Concentración: ", antibiotico1.concentracion)
    print("Frecuencia de la aplicación: ", antibiotico1.frecuencia_aplicacion)
    print("Tipo de producto: ", antibiotico1.tipo_animal)
    print("Precio: ", antibiotico1.valor_producto)

    print("Nombre del producto: ", antibiotico2.nombre_producto)
    print("Registro ICA: ", antibiotico2.registro_ICA)
    print(f"Dosis: {antibiotico2.dosis} mg/kg")
    print(f"Dosis para un {antibiotico2.tipo_animal} de {antibiotico2.peso} kg es de {dosis_calculada2} mg/kg")
    print("Concentración: ", antibiotico2.concentracion)
    print("Frecuencia de la aplicación: ", antibiotico2.frecuencia_aplicacion)
    print("Tipo de producto: ", antibiotico2.tipo_animal)
    print("Precio: ", antibiotico2.valor_producto)

    print("Nombre del producto: ", antibiotico3.nombre_producto)
    print("Registro ICA: ", antibiotico3.registro_ICA)
    print(f"Dosis: {antibiotico3.dosis} mg/kg")
    print(f"Dosis para un {antibiotico3.tipo_animal} de {antibiotico3.peso} kg es de {dosis_calculada3} mg/kg")
    print("Concentración: ", antibiotico1.concentracion)
    print("Frecuencia de la aplicación: ", antibiotico3.frecuencia_aplicacion)
    print("Tipo de producto: ", antibiotico3.tipo_animal)
    print("Precio: ", antibiotico3.valor_producto)
        
    assert antibiotico1.nombre_producto == "Oxitetraciclina"
    assert antibiotico1.registro_ICA == "1177-DB"
    assert antibiotico1.dosis == 10
    assert round(dosis_calculada1, 2) == 21.35     
    assert antibiotico1.concentracion == 200
    assert antibiotico1.frecuencia_aplicacion == Frecuencia_aplicacion.HORA
    assert antibiotico1.tipo_animal == Animal.BOVINO
    assert antibiotico1.peso == 427
    assert antibiotico1.valor_producto == 22800

    assert antibiotico2.nombre_producto == "Dihidroestreptomicina"
    assert antibiotico2.registro_ICA == "1910-DB"
    assert antibiotico2.dosis == 10
    assert round(dosis_calculada2, 2) == 21.96      
    assert antibiotico2.concentracion == 250
    assert antibiotico2.frecuencia_aplicacion == Frecuencia_aplicacion.HORAS
    assert antibiotico2.tipo_animal == Animal.PORCINO
    assert antibiotico2.peso == 549
    assert antibiotico2.valor_producto == 39600

    assert antibiotico3.nombre_producto == "Tilosina"
    assert antibiotico3.registro_ICA == "7731-MV"
    assert antibiotico3.dosis == 10
    assert round(dosis_calculada3, 2) == 24.15       
    assert antibiotico3.concentracion == 200
    assert antibiotico3.frecuencia_aplicacion == Frecuencia_aplicacion.DIA
    assert antibiotico3.tipo_animal == Animal.CARPINO
    assert antibiotico3.peso == 483
    assert antibiotico3.valor_producto == 34900