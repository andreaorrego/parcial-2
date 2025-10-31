class Clientes:
    def __init__ (self):
        self.nombre_cliente: str = ""
        self.cedula: str = ""

cliente1 = Clientes()
cliente1.nombre_cliente = "Juan Perez"
cliente1.cedula = "1234567890"

if __name__ == "__main__":
    print ("Nombre del cliente: ", cliente1.nombre_cliente)
    print ("Cédula del cliente: ", cliente1.cedula)
        