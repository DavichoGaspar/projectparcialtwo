from Entidades.entidades import *
from Inputs.opcionesmenu import *
from GestionDatos.gestiondatos import *


class Core:
    def __init__(self):
        self.ent = Entrada()
        self.registrous = []
        self.menu = Retornodeopcion()
        self.veri = gestionDatos()



    def main(self):
        print("\t\t Menu Supermercado")
        listamenu = ("No afiliado", "Afiliado", "Listar")
        opc = self.menu.menuyop(listamenu)

        if opc == 1:
            print("\t\tCrear usuario")
            input("Presione <Enter> para registrarse\n\n")
            self.registro()
            self.main()


        elif opc == 2:
            print("Ingrese su cedula: ")
            self.main()

        elif opc == 3:
            self.listar()
            self.main()

    def registro(self):
        print("\t\t Registro de usuario")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cedula: ")
        edad = self.ent.Int("Edad: ")
        direccion = input("Direccion: ")
        self.user = Usuario(nombre, apellido, cedula, direccion, edad)
        obj = self.veri.Verificar(cedula, self.registrous)
        if obj != None:
            print("%Error=> Cedula ya existe! " + obj.getDatos()\
                    + "Intentelo de nuevo... :(")
        else:
            print("Usuario registrado!")
            self.registrous.append(self.user)

        input("<Enter> para continuar...")



    def consulta(self, cedula, lista):
        self.consul = self.veri.Verificar(cedula, lista)
        return self.consul

    def listar(self):
        print("\t\t Lista de afiliados")
        for indice in range(len(self.registrous)):
            print(self.registrous[indice].getDatos())
        print("\n\n")