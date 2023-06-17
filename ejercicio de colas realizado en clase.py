class Clientes:
    def __init__(self, nombre, correoElectronico, peticion):
        self.nombre = nombre
        self.correoElectronico = correoElectronico
        self.peticion = peticion

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCorreoElectronico(self):
        return self.correoElectronico

    def setCorreoElectronico(self, correoElectronico):
        self.correoElectronico = correoElectronico

    def getPeticion(self):
        return self.peticion

    def setPeticion(self, peticion):
        self.peticion = peticion


class ColaBancos:
    def __init__(self):
        self.clientes = []

    def llegadaCliente(self, cliente):
        self.clientes.append(cliente)

    def atenderCliente(self):
        if self.clientes:
            cliente = self.clientes.pop(0)
            print("Atendiendo cliente:", cliente.getNombre())
        else:
            print("No hay clientes en la cola.")


def main():
    colaBancos = ColaBancos()
    nombre = input("Ingresa tu nombre: ")
    correoElectronico = input("Ingresa tu correo: ")
    peticion = input("Ingresa el motivo de tu consulta: ")
    colaBancos.llegadaCliente(Clientes(nombre, correoElectronico, peticion))


if __name__ == "__main__":
    main()
