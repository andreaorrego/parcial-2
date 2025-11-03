from Model.cliente import Clientes

def test_cliente():
    cliente1 = Clientes(nombre_cliente = "Andrea Orrego", cedula = 1192771677, celular = 3044683982)

    print("Nombre del cliente: ", cliente1.nombre_cliente)
    print("Cédula del cliente: ", cliente1.cedula)
    print("Celular del cliente: ", cliente1.celular)

    assert cliente1.nombre_cliente == "Andrea Orrego"
    assert cliente1.cedula == 1192771677
    assert cliente1.celular == 3044683982


